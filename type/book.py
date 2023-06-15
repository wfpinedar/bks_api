import typing
import strawberry
from conn.db import conn
from models.index import books
from strawberry.types import Info

@strawberry.type
class Book:
    id: int
    title: str
    subtitle: str
    author: str
    categories: str
    editor: str
    description: str
    image: str
    
@strawberry.type
class Query:
    @strawberry.field
    def book(self, id: int) -> Book:
        return conn.execute(books.select().where(books.c.id == id)).fetchone()
    
    @strawberry.field
    def books(self) -> typing.List[Book]:
        return conn.execute(books.select()).fetchall()
    
    @strawberry.field
    def query_book(self, field: str, value: str) -> Book:
        return conn.execute(books.select().where(getattr(books.c, field) == value)).fetchone()
    
    @strawberry.field
    def find_book(self, value: str) -> typing.List[Book]:
        query = books.select().where(
            (books.c.title == value) | 
            (books.c.subtitle == value) | 
            (books.c.author == value) | 
            (books.c.categories == value) | 
            (books.c.editor == value) | 
            (books.c.description == value) 
            )
        return conn.execute(query).fetchall()

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_book(self, 
                          title: str,
                          subtitle: str, 
                          author: str, 
                          categories: str, 
                          editor: str, 
                          description: str, 
                          image: str, 
                          info: Info) -> int:
        book =  {
            "title": title,
            "subtitle": subtitle,
            "author": author,
            "categories": categories,
            "editor": editor,
            "description": description,
            "image": image 
        } 
        result = conn.execute(books.insert(),book)
        conn.commit()
        return int(result.inserted_primary_key[0])
    
    @strawberry.mutation
    def update_book(self,
                    id: int,
                    title: str,
                    subtitle: str, 
                    author: str, 
                    categories: str, 
                    editor: str, 
                    description: str, 
                    image: str, 
                    info: Info) -> str:
        result = conn.execute(books.update().where(books.c.id == id), {
            "title": title,
            "subtitle": subtitle,
            "author": author,
            "categories": categories,
            "editor": editor,
            "description": description,
            "image": image 
        })
        conn.commit()
        print(result. returns_rows)
        return str(result.rowcount) + " Row(s) updated"
    
    @strawberry.mutation
    def delete_book(self, id: int) -> bool:
        result = conn.execute(books.delete().where(books.c.id == id))
        conn.commit()
        return result.rowcount > 0
from fastapi import APIRouter
from conn.db import conn 
from models.index import books
from type.book import Mutation, Query
from strawberry.asgi import GraphQL
import strawberry
book = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

book.add_route("/book", graphql_app)
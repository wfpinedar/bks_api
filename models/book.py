from conn.db import meta
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String

books = Table('books', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(50)),
    Column('subtitle', String(50)),
    Column('authors', String(50)),
    Column('categories', String(50)),
    Column('editor', String(50)),
    Column('description', String(50)),
    Column('image', String(50)),
)
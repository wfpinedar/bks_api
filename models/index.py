from importlib.metadata import metadata
from models.book import books
from conn.db import engine, meta

meta.create_all(engine)
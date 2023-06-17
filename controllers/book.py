from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from conn.db import conn 
from models.index import books
from models.user import User
from type.book import Mutation, Query
from strawberry.asgi import GraphQL
import strawberry
from utils.utils import user_is_valid
from middlewares.verify_token_route import VerifyTokenRoute
book = APIRouter(route_class=VerifyTokenRoute)

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

@book.post("/hello")
def hello():
    return {"ok": "Success Login"}

book.add_route("/book", graphql_app)
# book.add_websocket_route("/book", graphql_app)

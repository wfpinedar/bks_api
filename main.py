from fastapi import FastAPI
from controllers.main import book
app = FastAPI()

app.include_router(book)


# app.add_websocket_route("/graphql", graphql_app)
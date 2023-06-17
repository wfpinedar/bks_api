from fastapi import FastAPI
from dotenv import load_dotenv
from controllers.main import route, book
app = FastAPI()
load_dotenv()

app.include_router(route)
app.include_router(book)

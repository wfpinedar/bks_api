from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    subtitle: str
    authors: str
    categories: str
    editor: str
    description: str
    image: str
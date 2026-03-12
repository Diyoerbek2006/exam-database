from .db import SessionLocal
from .models import Author

def create_author(name: str, bio: str=None):

    db = SessionLocal()

    author = Author(name=name, bio=bio)

    db.add(author)
    db.commit()
    db.refresh(author)

    return author
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from .db import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    published_year = Column(Integer, nullable=True)
    isbn = Column(String(13), unique=True, nullable=True)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    author = relationship("Author", back_populates="books")
    borrows = relationship("Borrow", back_populates="book", cascade="all, delete-orphan")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    grade = Column(String(20), nullable=True)
    registered_at = Column(DateTime, default=datetime.now)

    borrows = relationship("Borrow", back_populates="student", cascade="all, delete-orphan")

class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    borrowed_at = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime, default=lambda: datetime.now() + timedelta(days=14))
    returned_at = Column(DateTime, nullable=True)

    student = relationship("Student", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")
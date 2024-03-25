from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)

# Define the SQLite database URL
DB_URL = "sqlite:///address_book.db"

# Create engine and create tables
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

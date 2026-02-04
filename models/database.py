from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

DATABASE_URL = "postgresql://{user}:{password}@{host}/{db}".format(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    db=os.getenv("DB_NAME")
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()

def create_tables():
    Base.metadata.create_all(bind=engine)


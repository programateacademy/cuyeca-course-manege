from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "sqlite:///database.sqlite"

engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
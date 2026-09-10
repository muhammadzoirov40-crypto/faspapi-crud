from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os

load_dotenv()


engine = create_engine(url=os.getenv('DATABASE_URL'))


SessionMaker  = sessionmaker(bind=engine)

class Base(DeclarativeBase): 
    pass



def get_db():
    db = SessionMaker()

    try:
        yield db
    finally:
        db.close()
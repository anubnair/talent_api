from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Set up the database engine and session
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def save_to_database(address, data):
    from app.models import PassportData
    passport_data = PassportData(address=address, data=data)
    session.add(passport_data)
    session.commit()


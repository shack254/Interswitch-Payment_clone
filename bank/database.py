import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")

connection_string = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_URL}:3306/corebank$01"

engine = create_engine(connection_string, echo=False)
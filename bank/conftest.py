import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def get_db_creds():
    DB_PASSWORD  = os.getenv("DB_PASSWORD")
    DB_URL = os.getenv("DB_URL")
    DB_USER = os.getenv("DB_USER")
    return DB_PASSWORD ,DB_URL ,DB_USER
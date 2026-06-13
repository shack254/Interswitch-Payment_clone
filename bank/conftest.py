import pytest
import os
from dotenv import load_dotenv
from bank.store import  get_account_details 

load_dotenv()

@pytest.fixture
def get_db_creds():
    DB_PASSWORD  = os.getenv("DB_PASSWORD")
    DB_URL = os.getenv("DB_URL")
    DB_USER = os.getenv("DB_USER")
    return DB_PASSWORD ,DB_URL ,DB_USER

@pytest.fixture
def account_bal_setup():
    return get_account_details("254700000001")

@pytest.fixture
def restricted_accont_setup():
    return get_account_details("254700000002")
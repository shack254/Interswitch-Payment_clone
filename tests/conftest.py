import pytest
import os
from dotenv import load_dotenv
from bank.store import  AccountDetails

load_dotenv()

@pytest.fixture
def get_db_creds():
    DB_PASSWORD  = os.getenv("DB_PASSWORD")
    DB_URL = os.getenv("DB_URL")
    DB_USER = os.getenv("DB_USER")
    return DB_PASSWORD ,DB_URL ,DB_USER

@pytest.fixture
def account_setup():
    account = AccountDetails.from_account_table("254700000001")
    return account

@pytest.fixture
def restricted_account_setup():
    account = AccountDetails.from_account_table("254700000002")
    return account



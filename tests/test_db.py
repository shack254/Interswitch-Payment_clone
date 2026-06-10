import pytest
from bank.store import  get_account_balance 
from sqlalchemy import create_engine, text
import os


#@pytest.fixture

#@pytest.fixture
#def db_setup():
#    connection_string = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_URL}:3306/corebank$01"
#    engine = create_engine(connection_string, echo=True)

@pytest.fixture
def account_bal_setup():
    return get_account_balance("254700000001")

def test_account_balance(account_bal_setup):
    assert account_bal_setup == '100000.00'

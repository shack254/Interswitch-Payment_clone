import pytest
from bank.store import  AccountDetails 
from bank.database import engine


@pytest.fixture
def account_setup():
    with engine.connect() as connection:
        account = AccountDetails.from_account_table(connection,"254700000001")
        return  account

@pytest.fixture
def restricted_account_setup():
    with engine.connect() as connection:
        account = AccountDetails.from_account_table(connection,"254700000002")
        return account



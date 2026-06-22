import pytest
from bank.store import  InsufficientFundsError ,AccountRestrictedError
from sqlalchemy import create_engine
from bank.database import engine


def test_debit_account(account_setup):
    with engine.begin() as connection:
        account =  account_setup
        amount = 100
        expected_balance = account.balance - amount
        assert account.debit(connection,amount) == expected_balance

def test_insuffince_funds(account_setup):
    with engine.begin() as connection:
        amount = 1000000
        with pytest.raises(InsufficientFundsError):
            account_setup.debit(connection,amount)

def test_debit_account_restiction(restricted_account_setup):
    with engine.begin() as connection:
        with pytest.raises(AccountRestrictedError):
            restricted_account_setup.debit(connection,100)
        
def test_credit_account(account_setup):
    with engine.begin() as connection:
        amount = 100
        expected_balance = account_setup.balance + amount
        assert account_setup.credit(connection,amount) == expected_balance

def test_credit_account_restiction(restricted_account_setup):
    with engine.begin() as connection:
        with pytest.raises(AccountRestrictedError):
            restricted_account_setup.debit(connection,100)
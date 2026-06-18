import pytest
from bank.store import  InsufficientFundsError ,AccountRestrictedError


@pytest.fixture
def credit_account_setup(account_setup):
    amount = 100.00
    return account_setup.credit_account(amount)

@pytest.fixture
def account_credit_restriction_setup(restricted_account_setup):
    return restricted_account_setup.credit_account(100)

def test_debit_account(account_setup):
    amount = 100
    expected_balance = account_setup.balance - amount
    assert account_setup.debit_account(amount) == expected_balance

def test_insuffince_funds(account_setup):
    amount = 1000000
    with pytest.raises(InsufficientFundsError):
        account_setup.debit_account(amount)

def test_debit_account_restiction(restricted_account_setup):
    with pytest.raises(AccountRestrictedError):
        restricted_account_setup.debit_account(100)
        
def test_credit_account(account_setup):
    amount = 100
    expected_balance = account_setup.balance + amount
    assert account_setup.credit_account(amount) == expected_balance

def test_credit_account_restiction(restricted_account_setup):
    with pytest.raises(AccountRestrictedError):
        restricted_account_setup.debit_account(100)
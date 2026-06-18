import pytest
from bank.store import  InsufficientFundsError ,AccountRestrictedError

def test_debit_account(account_setup):
    amount = 100
    expected_balance = account_setup.balance - amount
    assert account_setup.debit(amount) == expected_balance

def test_insuffince_funds(account_setup):
    amount = 1000000
    with pytest.raises(InsufficientFundsError):
        account_setup.debit(amount)

def test_debit_account_restiction(restricted_account_setup):
    with pytest.raises(AccountRestrictedError):
        restricted_account_setup.debit(100)
        
def test_credit_account(account_setup):
    amount = 100
    expected_balance = account_setup.balance + amount
    assert account_setup.credit(amount) == expected_balance

def test_credit_account_restiction(restricted_account_setup):
    with pytest.raises(AccountRestrictedError):
        restricted_account_setup.debit(100)
import pytest
from bank.store import  get_account_details ,debit_account
from sqlalchemy import create_engine, text
import os


@pytest.fixture
def debit_account_setup(account_bal_setup):
    amount = '1000'
    debit_account(amount,account_bal_setup["balance"],account_bal_setup["id"],account_bal_setup["restictions"])
    return get_account_details(account_bal_setup["id"])

@pytest.fixture
def insuffince_funds_setup(account_bal_setup):
    amount = '1000000'
    return debit_account(amount,account_bal_setup["balance"],account_bal_setup["id"],account_bal_setup["restictions"])

@pytest.fixture
def account_restriction_setup(restricted_accont_setup):
    return debit_account( 100,restricted_accont_setup["balance"],restricted_accont_setup["id"],restricted_accont_setup["restictions"]    )

def test_debit_account(account_bal_setup, debit_account_setup):
    expected_balance = float(account_bal_setup["balance"]) - 1000
    assert float(debit_account_setup["balance"]) == expected_balance

def test_insuffince_funds(insuffince_funds_setup):
    debit_account  = insuffince_funds_setup
    assert debit_account["Response"] == "INSUFFICIENT_FUNDS"

def test_account_restiction(account_restriction_setup):
    debit_account  = account_restriction_setup
    assert debit_account["Response"] == "DEBIT_ACCOUNT_RESTRICTED"
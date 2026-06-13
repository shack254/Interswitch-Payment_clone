import pytest
from bank.store import  get_customer_details

@pytest.fixture
def setup_customer_details():
    return get_customer_details("254700000001")

@pytest.fixture
def setup_customer_does_not_exist():
    return get_customer_details("25470000001")

def test_customer_details(setup_customer_details):
    assert setup_customer_details["id"] == 'CUST001'

def test_customer_does_not_exist(setup_customer_does_not_exist):
    assert setup_customer_does_not_exist == None
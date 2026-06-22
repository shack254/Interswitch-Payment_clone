from .store import AccountDetails 
from .database import engine
from sqlalchemy import text

inward_account = "KES700000002" 

def inward_wire_transfer(request):
    with engine.connect() as connection:
        debit_account = AccountDetails.from_account_table(request.debit_account)
        credit_account = AccountDetails.from_account_table(request.inward_account)
        debit_account.debit(request.amount)
        credit_account.credit(request.amount)
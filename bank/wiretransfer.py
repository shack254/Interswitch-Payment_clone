from .store import AccountDetails ,populate_statement_entry
from .database import engine

inward_suspence_account = "KES700000002" 

def inward_wire_transfer(request):
    with engine.begin() as connection:
        debit_account = AccountDetails.from_account_table(connection,request.debit_account)
        credit_account = AccountDetails.from_account_table(connection,inward_suspence_account)
        debit_account.debit(connection,request.amount)
        credit_account.credit(connection,request.amount)
        return populate_statement_entry(connection,request ,debit_account.account_number,credit_account.account_number)
from sqlalchemy import  text
import random
from .database import engine
import time
import random
import string
class AccountNotFoundError(Exception): 
    def __init__(self, account_number):
        super().__init__(f"Account {account_number} not found.")
        self.account_number
        
class InsufficientFundsError(Exception): pass
class AccountRestrictedError(Exception): pass
class AccountDetails:
    
    def __init__(self , account_number:str,
                 balance:float, 
                 account_name:str , 
                 customer_id:str , 
                 restictions:str|None =None):
        
        self.account_number = account_number
        self.balance = balance
        self.account_name = account_name
        self.customer_id= customer_id
        self.restictions = restictions

    @classmethod
    def from_account_table(cls,connection,account_number):
        query = text("select * from account where id = :id")
        result = connection.execute(query, {"id": f"{account_number}"})
        account = result.mappings().first()
        
        if account is None:
            raise AccountNotFoundError("Account does not exist")
        
        return cls(account["id"],
                    float(account["balance"]) , 
                    account["Account_name"],
                    account["customer_id"] ,
                    account["restictions"])

    def debit(self ,connection,amount:float) :
        if self.balance < amount :
            raise InsufficientFundsError("Insufficient funds.")
        
        if self.restictions is not None:
            raise AccountRestrictedError("Debit restricted on this account.")
        
        if self.balance > amount  and self.restictions  is None:
            self.balance -= amount
            update_balance_query = text(
                "update corebank$01.account set balance = :balance where id = :id "
                )
            connection.execute(
                update_balance_query,
                {"balance" : float(self.balance) , "id" : self.account_number }
                )
                
            return self.balance
    

    def credit(self ,connection, amount :float):
        if self.restictions is not None:
            raise AccountRestrictedError("Credit restricted on this account.")
        else :
            self.balance += amount
            update_balance_query = text(
                "update corebank$01.account set balance = :balance where id = :id "
                )
            connection.execute(update_balance_query,
                                {"balance" : float(self.balance) , "id" : self.account_number }
                                )
            return self.balance

def populate_stmt_id():
    date = time.strftime("%y%m%d", time.localtime())
    alphabet = string.ascii_uppercase
    return f"UQ{date}{"".join(random.choices(alphabet , k =5))}"    
    
        
def get_customer_details(account_number):
    with engine.connect() as connection:
        query  = text("select c.* from account a, customer c where a.id = :id and c.id = a.customer_id")
        result =  connection.execute(query, {"id": f"{account_number}"})
        customer_details = result.mappings().first() 
        return customer_details 

def get_account_details(requst):
    with engine.connect() as connection:
        return AccountDetails.from_account_table(connection,requst.account)

def populate_statement_entry(connection,request ) -> str: 
    statement_id = populate_stmt_id()
    query = text(
        "INSERT INTO corebank$01.statement "
        "(id, credit_account, transaction_date, transaction_timestamp, amount, description, debit_account) "
        "VALUES "
        "(:id, :credit_account, :transaction_date, :transaction_timestamp, :amount, :description, :debit_account)"
        )
    connection.execute(query,{"id": statement_id,
                                "credit_account": request.creditaccount,
                                "transaction_date": time.strftime("%Y-%m-%d", time.localtime()),
                                "transaction_timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                "amount": request.amount,
                                "description": request.description,
                                "debit_account": request.debitaccount,
                            })
    return statement_id

def internaltransfer_core(request ):
     with engine.begin() as connection:
        debitaccount = AccountDetails.from_account_table(connection,request.debitaccount)
        creditaccount = AccountDetails.from_account_table(connection,request.creditaccount)
        debitaccount.debit(connection,request.amount)
        creditaccount.credit(connection,request.amount)
        return  populate_statement_entry(connection,request)
        


    
 
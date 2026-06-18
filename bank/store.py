import os
from sqlalchemy import create_engine, text
import random
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD  = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")

connection_string = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_URL}:3306/corebank$01"
engine = create_engine(connection_string, echo=False)

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
        self.accountname = account_name
        self.customer_id= customer_id
        self.restictions = restictions

    @classmethod
    def from_account_table(cls,account_number):
        with engine.connect() as connection: 
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

    def debit(self , amount:float) :
        if self.balance < amount :
            raise InsufficientFundsError("Insufficient funds.")
        
        if self.restictions is not None:
            raise AccountRestrictedError("Debit restricted on this account.")
        
        if self.balance > amount  and self.restictions  is None:
            self.balance -= amount
            with engine.begin() as connection:
                update_balance_query = text(
                    "update corebank$01.account set balance = :balance where id = :id "
                    )
                connection.execute(
                    update_balance_query,
                    {"balance" : float(self.balance) , "id" : self.account_number }
                    )
                
            return self.balance
    

    def credit(self , amount :float):
        if self.restictions is not None:
            raise AccountRestrictedError("Credit restricted on this account.")
        else :
            self.balance += amount
            with engine.begin() as connection:
                update_balance_query = text(
                    "update corebank$01.account set balance = :balance where id = :id "
                    )
                connection.execute(update_balance_query,
                                   {"balance" : float(self.balance) , "id" : self.account_number }
                                   )
            return self.balance



# def get_account_details(account_number):
#         with engine.connect() as connection: 
#             query = text("select * from account where id = :id")
#             result = connection.execute(query, {"id": f"{account_number}"})
#             account = result.mappings().first()
#             return account

def get_customer_details(account_number):
    with engine.connect() as connection:
        query  = text("select c.* from account a, customer c where a.id = :id and c.id = a.customer_id")
        result =  connection.execute(query, {"id": f"{account_number}"})
        customer_details = result.mappings().first() 
        return customer_details



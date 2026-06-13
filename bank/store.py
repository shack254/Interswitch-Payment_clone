import os
from sqlalchemy import create_engine, text
import random
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD  = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")
ACCOUNT_RANGE = 2E10
CUST_LOW_RANGE = 1E10
CUST_HIGH_RANGE = 9E10

connection_string = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_URL}:3306/corebank$01"
engine = create_engine(connection_string, echo=False)

def get_account_details(account_number):
    with engine.connect() as connection: 
        query = text("select * from account where id = :id")
        result = connection.execute(query, {"id": f"{account_number}"})
        account = result.mappings().first()
        return account

def get_customer_details(account_number):
    with engine.connect() as connection:
        query  = text("select c.* from account a, customer c where a.id = :id and c.id = a.customer_id")
        result =  connection.execute(query, {"id": f"{account_number}"})
        customer_details = result.mappings().first()
        return customer_details


def debit_account(amount,balance , account_number ,restictions) :
    balance = float(balance)
    amount = float(amount)

    if balance < amount :
        return {"Response" : "INSUFFICIENT_FUNDS"}
    if restictions is not None:
        return {"Response" : "DEBIT_ACCOUNT_RESTRICTED"}
    if balance > amount  and restictions  is None:
        new_bal = int(balance) - int(amount) 
        with engine.begin() as connection:
            update_balance_query = text("update corebank$01.account set balance = :balance where id = :id ")
            connection.execute(update_balance_query,{"balance" : float(new_bal) , "id" : account_number })
        return {"Response" : "ACCOUNT_DEBITED" , "balance" : balance , "amount" : amount}
 

def credit_account(amount ,balance , account_number , restictions):
    balance = float(balance)
    amount = float(amount) 
    if restictions is not None:
        return {"Response" : "CREDIT_ACCOUNT_RESTRICTED"}
    else :
        new_bal = balance + amount
        with engine.begin() as connection:
            update_balance_query = text("update corebank$01.account set balance = :balance where id = :id ")
            connection.execute(update_balance_query,{"balance" : float(new_bal) , "id" : account_number })
        return {"Response" : "ACCOUNT_CERDITED" , "balance" : new_bal , "amount" : amount}
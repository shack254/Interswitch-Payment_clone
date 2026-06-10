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

def get_account_balance(account_number):
    with engine.connect() as connection: 
        query = text("select balance from account where id = :id")
        result = connection.execute(query, {"id": f"{account_number}"})
        account = result.mappings().first()
        return account["balance"]

def generate_account_details():
    account_dict={
        "id":  random.randint(ACCOUNT_RANGE , ACCOUNT_RANGE ),
        "balance" : "0" ,
        "Account_name" : "name",
        "customer_id" : f"C-{random.randint(CUST_LOW_RANGE,CUST_LOW_RANGE)}",
        "restictions" : "NONE"
    }
    return account_dict


def create_new_customer(custom_details,generate_account_details):
    with engine.begin() as connection:
        customer_query = text("INSERT INTO corebank$01.customer (id, Name, legal_id, age, phone_number, email_adress)" \
        " VALUES (id:,Name:,legal_id:,age:,phone_number:,email_adress:")
        account_query =  text("INSERT INTO corebank$01.account (id, balance, Account_name, customer_id, restictions)" \
        "VALUES (id:, balance:, Account_name:,customer_id:, restictions:)")
        connection.execute(customer_query,custom_details)
        connection.execute(account_query,generate_account_details) # create a func to populate  account_details

def  delete_customer():
    pass


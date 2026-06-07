import os
from sqlalchemy import create_engine, text

DB_PASSWORD  = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")

connection_string = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_URL}:3306/corebank$01"

engine = create_engine(connection_string, echo=True)

def get_account_balance(account_number):
    with engine.connect() as connection: 
        query = text("select balance from account where id = :id")
        result = connection.execute(query, {"id": f"{account_number}"})
        for row in result.mappings():
            print(row["balance"])

def create_new_customer(custom_details,account_details):
    with engine.connect() as connection:
        customer_query = text("INSERT INTO corebank$01.customer (id, Name, legal_id, age, phone_number, email_adress)" \
        " VALUES (id:,Name:,legal_id:,age:,phone_number:,email_adress:")
        account_query =  text("INSERT INTO corebank$01.account (id, balance, Account_name, customer_id, restictions)" \
        "VALUES (id:, balance:, Account_name:,customer_id:, restictions:)")
        connection.execute(customer_query,custom_details)
        connection.execute(account_query,account_details) # create a func to populate  account_details

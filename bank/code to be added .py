
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

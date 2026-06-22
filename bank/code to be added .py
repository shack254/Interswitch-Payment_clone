
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

class statement:
    def __init__(self ,credit_account:str, 
                 transaction_date, 
                 transaction_timestamp,
                 amount, 
                 debit_account,
                 statement_id = None,
                 description = None,
                 external_debit_account = None, 
                 external_credit_account = None):
        self.statement_id = statement_id 
        self.credit_account = credit_account
        self.transaction_date = transaction_date
        self.transaction_timestamp = transaction_timestamp
        self.amount = amount
        self.description = description
        self.debit_account = debit_account
        self.external_debit_account = external_debit_account
        self.external_credit_account = external_credit_account
#from fastapi import FastAPI
#
#app = FastAPI()
#
#@app.get("/")
#def health_check():
#    return {"status": "bank service running"}

from store import  get_account_balance 

balance = get_account_balance("254700000001")
print(balance)


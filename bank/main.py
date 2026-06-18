from fastapi import FastAPI ,HTTPException ,status
from fastapi.responses import JSONResponse
from bank.schemas import AccountDetailsRequst ,AccountDetailsResponse  ,InteranTranferResponse ,InteranTranferRequst
from bank.store import AccountDetails ,AccountNotFoundError ,InsufficientFundsError ,AccountRestrictedError

app = FastAPI()

@app.get("/")
def health_check():
   return {"status": "bank service running"}

@app.post("/getaccountdetails/", response_model=AccountDetailsResponse)
def getaccountdetails( accountrequst:AccountDetailsRequst):
    try :
        accountdetailsresponse = AccountDetails.from_account_table(accountrequst.account)
        return accountdetailsresponse
    except AccountNotFoundError :
        raise HTTPException(status_code=404, detail={
        "status": "FAILED",
        "message": "Account not found"
    })

@app.post("/internaltransfer/" , response_model = InteranTranferResponse)
def internaltransfer(requst:InteranTranferRequst):
   try:
       debitaccount = AccountDetails.from_account_table(requst.debitaccount)
       creditaccount = AccountDetails.from_account_table(requst.creditaccount)
       debitaccount.debit(requst.amount)
       creditaccount.credit(requst.amount)
       return { 
            "status": "SUCCESS",
            "refrence": "FT"
       }       
   except AccountNotFoundError :
        raise HTTPException(status_code=404, detail={
        "status": "FAILED",
        "message": "Account not found"
    })
   except InsufficientFundsError:
       raise HTTPException(status_code=200, detail={
        "status": "FAILED",
        "message": f"InsufficientFundsError"
    })
   except AccountRestrictedError :
       raise HTTPException(status_code=200, detail={
        "status": "FAILED",
        "message": f"AccountRestrictedError"
    })
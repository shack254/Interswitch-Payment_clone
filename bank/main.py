from fastapi import FastAPI ,HTTPException ,status
from fastapi.responses import JSONResponse
from bank.schemas import AccountDetailsRequst ,AccountDetailsResponse  ,InteranTranferResponse ,InteranTranferRequst
from bank.store import get_account_details

app = FastAPI()

@app.get("/")
def health_check():
   return {"status": "bank service running"}

@app.post("/getaccountdetails/", response_model=AccountDetailsResponse)
def getaccountdetails( accountrequst:AccountDetailsRequst):
   accountdetailsresponse = get_account_details(accountrequst.account)
   if not accountdetailsresponse :
      raise HTTPException(status_code=404, detail={
        "status": "FAILED",
        "message": "Account not found"
    })
   return accountdetailsresponse
    
@app.post("/internaltransfer" , response_model = InteranTranferResponse)
def internaltransfer(requst=InteranTranferRequst):
   pass
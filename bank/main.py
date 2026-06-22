from fastapi import FastAPI ,HTTPException ,status
from fastapi.responses import JSONResponse
from bank.schemas import( AccountDetailsRequst ,AccountDetailsResponse  ,InteranTranferResponse ,
                         InteranTranferRequst,IncomingWireTransferRequest,IncomingWireTransferResponse)
from bank.store import (get_account_details ,AccountNotFoundError ,InsufficientFundsError ,
                        AccountRestrictedError , internaltransfer_core
)
from bank.wiretransfer import inward_wire_transfer
app = FastAPI()

@app.get("/")
def health_check():
   return {"status": "bank service running"}

@app.post("/getaccountdetails/", response_model=AccountDetailsResponse)
def getaccountdetails( accountrequst:AccountDetailsRequst):
    try :
        accountdetailsresponse = get_account_details(accountrequst.account)
        return accountdetailsresponse
    except AccountNotFoundError :
        raise HTTPException(status_code=404, detail={
        "status": "FAILED",
        "message": "Account not found"
    })

@app.post("/internaltransfer/" , response_model = InteranTranferResponse)
def internaltransfer(requst:InteranTranferRequst):
   try:
       Ref = internaltransfer_core(requst)
       return { 
            "status": "SUCCESS",
            "refrence": Ref
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

@app.post("/IncomingWireTransfer/" , response_model = IncomingWireTransferResponse)
def IncomingWireTransfer(requst:IncomingWireTransferRequest):
    try:
       Ref = inward_wire_transfer(requst)
       return { 
            "status": "SUCCESS",
            "refrence": Ref
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
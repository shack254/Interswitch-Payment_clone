from pydantic import BaseModel

class AccountDetailsRequst(BaseModel):
    account:str

class AccountDetailsResponse(BaseModel):
    id:str
    balance:int
    Account_name:str
    customer_id:str
    restiction: str | None = None

class InteranTranferRequst(BaseModel):
    debitaccount: str
    creditaccount :str
    amount : float

class InteranTranferResponse(BaseModel):
    balance: str
    status :str
    refrence : str
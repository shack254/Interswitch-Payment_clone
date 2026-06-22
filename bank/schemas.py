from pydantic import BaseModel

class AccountDetailsRequst(BaseModel):
    account:str

class AccountDetailsResponse(BaseModel):
    account_number:str
    balance:int
    account_name:str
    customer_id:str
    restiction: str | None = None


class InteranTranferRequst(BaseModel):
    debitaccount: str
    creditaccount :str
    amount : float
    description:str | None = None

class InteranTranferResponse(BaseModel):
    status :str
    refrence : str = 'ft'
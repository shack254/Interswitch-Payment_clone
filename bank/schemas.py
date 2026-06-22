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
    refrence:str = 'ft'
    
class WireTransferRequest(BaseModel):
    debit_account: str
    credi_taccount :str
    amount : float
    description:str | None = None
    external_debit_account: str | None = None
    external_credit_account: str | None = None
    from_bank : str | None = None
    to_bank  : str | None = None

class WireTransferResponse(InteranTranferResponse):
    pass
    
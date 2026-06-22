from pydantic import BaseModel , Field
from pydantic.json_schema import SkipJsonSchema

class AccountDetailsRequst(BaseModel):
    account:str

class AccountDetailsResponse(BaseModel):
    account_number:str
    balance:int
    account_name:str
    customer_id:str
    restiction: str | None = None
    
class  BaseTranferRequst(BaseModel):
    debit_account: str | None
    credit_account :str | None
    amount : float
    description:str | None
    external_debit_account: SkipJsonSchema[str | None] = Field(default=None , exclude=True)
    external_credit_account: SkipJsonSchema[str | None] = Field(default=None , exclude=True)
    from_bank:SkipJsonSchema[str | None] = Field(default=None , exclude=True)
    to_bank:SkipJsonSchema[str | None] = Field(default=None , exclude=True)
class InteranTranferRequst(BaseTranferRequst):
    pass
    
class InteranTranferResponse(BaseModel):
    status :str
    refrence:str = 'ft'
    
class IncomingWireTransferRequest(BaseTranferRequst):
    credit_account:SkipJsonSchema[str | None] = Field(default=None , exclude=True)
    external_debit_account: str 
    from_bank:str
    to_bank:str
class IncomingWireTransferResponse(InteranTranferResponse):
    pass

class OutwardWireTransferRequest(BaseTranferRequst):
    debit_account: SkipJsonSchema[str | None] = Field(default=None , exclude=True)
    external_credit_account: str
    from_bank:str
    to_bank:str
class OutwardWireTransferResponse(InteranTranferResponse):
    pass
    
from pydantic import BaseModel
 
class Address(BaseModel):
    id: int
    address:str
    city: str
    state: str
    zip: int

class Customer(BaseModel):
    id: int
    firstname: str
    lastname: str
    address_id: int
    email: str

class Account(BaseModel):
    id: str
    account_number: str
    customer_id: int
    balance: float
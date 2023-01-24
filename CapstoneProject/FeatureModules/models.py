from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
 
class Address(BaseModel):
    id: int
    city: str
    state: str
    zip: int

class Customer(BaseModel):
    id: int
    lastname: str
    address_id: int
    email: str

class Account(BaseModel):
    id: str
    customer_id: int
    balance: float
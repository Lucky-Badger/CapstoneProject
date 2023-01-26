from typing import Union
from fastapi import FastAPI
from FeatureModules.Services import accountService


app = FastAPI()

@app.post("/createAccount/{id}/{address}/{city}/{state}/{zip}")
def create_account(id: int, address, city, state, zip):
    acctService = accountService()
    acctService.createAccount(id, address, city, state, zip)
    return {"Hello": "World"}


@app.get("/getAccounts")
def get_all_account(item_id: int, q: Union[str, None] = None):
    acctService = accountService()
    accountList = acctService.getAllAccounts()
    return {"account_lists": accountList}

@app.get("/getAccount/{accountId}")
def get_account(account_id: int,):
    acctService = accountService()
    account = acctService.getAccount(account_id)
    first_name = account.firstName
    last_name = account.lastName
    address = account.address
    email_address = account.emailAddress
    return {"first_name": first_name, "last_name": last_name, "address": address, "email_address": email_address }

@app.get("/withdraw/{account_Id}/{amount}")
def withdraw(account_Id: int):
    acctService = accountService()
    accountList = acctService.getAllAccounts()
    return {"success": "success!"}



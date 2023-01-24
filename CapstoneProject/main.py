from typing import Union

from fastapi import FastAPI
import { accountService} from ./Services/accountService

<<<<<<< HEAD
app = FastAPI()
accountService = AcountService()
=======

accountService = AcountService()
>>>>>>> origin

app = FastAPI()

@app.post("/createAccount/{id}/{address}/{city}/{state}/{zipcode}")
def create_account(id: int, address, city, state, zipcode):
    accountService.createAccount(id, address, city, state, zipcode)
    return {"Hello": "World"}


@app.get("/getAccounts")
def get_all_account(item_id: int, q: Union[str, None] = None):
    accountList = accountService.getAllAccounts()
    return {"account_lists": accountList}

@app.get("/getAccount/{accountId}")
def get_account(account_id: int,):
    account = accountService.getAccount(account_id)
    first_name = account.firstName
    last_name = account.lastName
    address = account.address
    email_address = account.emailAddress
    return {"first_name": first_name, "last_name": last_name, "address": address, "email_address": email_address }

@app.get("/withdraw/{account_Id}/{amount}")
def withdraw(account_Id: int):
    accountList = accountService.getAllAccounts()
    return {"success": "success!"}



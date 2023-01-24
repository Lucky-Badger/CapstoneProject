from typing import Union

from fastapi import FastAPI
import { accountService} from ./Services/accountService

app = FastAPI()
accountService = AcountService()

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
def get_account(account_id: int, q: Union[str, None] = None):
    account = accountService.getAccount(account_id).fetchall(
    first_name = account.firstName
    last_name = account.lastName
    address = account.address
    email_address = account.emailAddress
    return {"account_lists": accountList, }

import uvicorn
from typing import Union
from fastapi import FastAPI
from FeatureModules.models import Account
from FeatureModules.Services.accountService import AccountService
from FeatureModules.Repositories.account_repo import AccountRepository
from FeatureModules.Repositories.customer_repo import CustomerRepository
from FeatureModules.Repositories.address_repo import AddressRepository
from typing import List
from FeatureModules.Services import accountService


app = FastAPI()
address_repository = AddressRepository()
customer_repository = CustomerRepository()
account_repository = AccountRepository()
account_service = AccountService(account_repository, customer_repository, address_repository)

@app.post("/createAccount/{id}/{address}/{city}/{state}/{zip}")
def create_account(id: int, address, city, state, zip):
    accountService = accountService()
    accountService.createAccount(id, address, city, state, zip)
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


@app.post('/api/accounts')
async def open_account(account: Account) -> Account:
    if account.balance < 25.0:
        raise ValueError('$25.00 minimum required on account opening')
    return account_service.open_account(account)

@app.get('/api/accounts', response_model=List[Account])
async def retrieve_accounts() -> List[Account]:
    return account_service.get_all_accounts()

@app.get('/api/accounts/{account_number}')
async def retrieve_account(account_number) -> Account:
    return account_service.get_account(account_number)

@app.put('/api/accounts/{account_number}/withdraw/{amount}')
async def withdraw(account_number, amount) -> Account:
    mod = float(amount)
    if mod <= 0:
        raise ValueError('Invalid amount specified on withdrawal')
    account = account_service.get_account(account_number)
    if mod > account.balance:
        raise ValueError('Withdrawal not completed because of potential overdraw')
    return account_service.withdraw(account_number, mod)

@app.put('/api/accounts/{account_number}/deposit/{amount}')
async def deposit(account_number, amount) -> Account:
    mod = float(amount)
    if mod <= 0:
        raise ValueError('Invalid amount specified on depost')
    return account_service.deposit(account_number, mod)

@app.delete('/api/accounts/{account_number}')
async def close_account(account_number) -> None:
    account_service.close_account(account_number)

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8100,reload=True)

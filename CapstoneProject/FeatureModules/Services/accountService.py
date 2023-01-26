from FeatureModules.models import Account
from FeatureModules.Repositories.account_repo import AccountRepository

class accountService():
  
  def __init__(self):
      return

  def createAccount(id2, account_number2, customer_id2, balance):
    acctRepo = AccountRepository()
    account = Account(id = id2, account_number = account_number2, customer_id = customer_id2, balance = balance)
    acctRepo.insert(account)
    return
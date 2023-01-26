from FeatureModules.models import Account
from FeatureModules.Repositories.account_repo import AccountRepository
from FeatureModules.Repositories.customer_repo import CustomerRepository
from FeatureModules.Repositories.address_repo import AddressRepository 


class AccountService():
    def __init__(self, account_repository: AccountRepository, 
            customer_repository: CustomerRepository,
            address_repository: AddressRepository) -> None:
        self.account_repository = account_repository
        self.customer_repository = customer_repository
        self.address_repository = address_repository

    def open_account(self, account: Account) -> Account:
        address = self.address_repository.insert(account.customer_id.address_id)
        account.customer_id.address_id = address
        customer = self.customer_repository.insert(account.customer_id)
        account.customer_id = customer
        return self.account_repository.insert(account)

    def get_all_accounts(self) -> 'list[Account]':
        accounts = self.account_repository.get_all()
        for account in accounts:
            account.customer_id = self.customer_repository.get_by_id(account.customer_id.id)
            account.customer_id.address_id = self.address_repository.get_by_id(account.customer_id.address_id.id)
        return accounts

    def get_account(self, account_number: str) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.customer_id = self.customer_repository.get_by_id(account.customer_id.id)
        account.customer_id.address_id = self.address_repository.get_by_id(account.customer_id.address_id.id)
        return account

    def withdraw(self, account_number: str, amount: float) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.balance -= amount
        self.account_repository.update(account)
        return self.get_account(account_number)

    def deposit(self, account_number: str, amount: float) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.balance += amount
        self.account_repository.update(account)
        return self.get_account(account_number)

    def close_account(self, account_number: str) -> None:
        account = self.get_account(account_number)
        self.account_repository.delete(account.id)
        self.customer_repository.delete(account.customer_id.id)
        self.address_repository.delete(account.customer_id.address_id.id)
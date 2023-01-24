import psycopg2
from models import Account

class AccountRepository():
    def insert(self, account:Account) -> Account:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO account
                    (AccountNumber, CustomerID, CurrentBalance) VALUES
                    (%(id)s, %(customer_id)s, %(balance)s)
                    RETURNING id""",{
                    'id': account.id,
                    'customer_id': account.customer_id,
                    'balance': account.balance
                    }
                )
                account.id = cursor.fetchone()[0]
            return account

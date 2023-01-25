import psycopg2
from models import Customer

class CustomerRepository():
    def insert(self, customer:Customer) -> Customer:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO account
                    (PrimaryID, FirstName, LastName, AddressID, Email) VALUES
                    (%(id)s, %(firstname)s, %(lastname)s, %(address_id)s, %(email)s)
                    RETURNING id""",{
                    'id': customer.id,
                    'firstname': customer.firstname,
                    'lastname': customer.lastname,
                    'address_id': customer.address_id,
                    'email': customer.email
                    }
                )
                customer.id = cursor.fetchone()[0]
            return customer
import psycopg2
from FeatureModules.models import Customer, Address

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
    def get_by_id(self, id) -> Customer:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT PrimaryID, FirstName, LastName, AddressID, Email FROM 
                        customer WHERE ID=%(customer_id)s
                    """, {
                    'customer_id': id
                }
                )
                row = cursor.fetchone()
        return Customer.construct(id=row[0], first_name=row[1], last_name=row[2], address=Address.construct(id=row[3]), email_address=row[4])

    def delete(self, id) -> None:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM customer WHERE ID=%(customer_id)s
                    """, {
                    'customer_id': id
                }
                )
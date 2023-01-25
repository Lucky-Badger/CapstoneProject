import psycopg2
from models import Address

class AddressRepository():
    def insert(self, address:Address) -> Address:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO address
                    (PrimaryID, Address, City, State, ZipCode) VALUES
                    (%(id)s, %(address)s, %(city)s, %(state)s, %(zip)s)
                    RETURNING id""",{
                    'id': address.id,
                    'address_number': address.address,
                    'city': address.city,
                    'state': address.state,
                    'zip': address.zip
                    }
                )
                address.id = cursor.fetchone()[0]
            return address

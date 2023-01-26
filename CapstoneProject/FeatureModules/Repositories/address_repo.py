import psycopg2
from FeatureModules.models import Address

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
    def get_by_id(self, id) -> Address:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT PrimaryID, Address, City, State, ZipCode FROM 
                        address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )
                row = cursor.fetchone()
        return Address.construct(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])

    def delete(self, id) -> None:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )

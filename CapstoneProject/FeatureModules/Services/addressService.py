from models import Address
from Repositories.address_repo import AddressRepository

class addressService():
  
  def __init__(self):
      return

  def createAddress(id, address, city, state, zip):
    
    address_repo = AddressRepository()
    new_address = Address(id = id, address = address, city = city, state = state, zip = zip)
    address_repo.insert(new_address)
    return
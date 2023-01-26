from models import Address
from FeatureModules.Repositories.address_repo import AddressRepository

class addressService():
  
  def __init__(self):
      return
  


  def createAddress(id, address, city, state, zip):  
    address_repo = AddressRepository()
    new_address = createAddressHelper(id, address, city, state, zip)
    address_repo.insert(new_address)
    return new_address

def createAddressHelper(id, address, city, state, zip):
    newAddress = Address(id = id, address = address, city = city, state = state, zip = zip)
    return newAddress
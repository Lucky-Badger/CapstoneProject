from Services import addressService 
from Services import accountService

def test_createaddress():
    address = addressService.createAddressHelper(0, '245 Candyland', 'NY', 'NY', 12345)
    assert address.id == 0
    assert address.address == '245 Candyland'
    assert address.city == 'NY'
    assert address.state == 'NY'
    assert address.zip == 12345



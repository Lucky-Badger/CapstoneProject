from Services import addressService 

def func(x):
    return x + 1


def test_createaddress():
    address = addressService.createAddressHelper(0, 'test', 'test','test')
    assert address.id == 0
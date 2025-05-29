import pytest


def test_firstprogram():
    message ='Hello'
    # second argument is printed if assert failed
    assert message=='Hi',"Test failed because strings dont match"

def test_secondprogram():
    a=4
    b=5
    assert a+2==b,"condition failed failed"

@pytest.mark.skip # skip the tc while running
@pytest.mark.smoke
def test_printCreditCard():
    a = 4
    b = 5
    assert a + 2 == b, "condition failed failed"
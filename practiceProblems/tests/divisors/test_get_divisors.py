
import divisors.get_divisors as divisors

def test_get_divisors():
    #test to make sure the proper divisors are returned
    #  by spot checking different values
    divs = divisors.get(26)
    assert divs == [1,2,13,26]

    divs = divisors.get(100)
    assert divs == [1,2,4,5,10,20,25,50,100]

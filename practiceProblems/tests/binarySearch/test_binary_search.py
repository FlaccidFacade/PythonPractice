
import binarySearch.search as search

def test_get_divisors():
    
    a = [1,2,4,5,10,20,25,50,100]

    pos = search.iterate(a,10)

    assert pos == 4

    a = [1,2,4,5,8,10,20,25,50,100]
    
    pos = search.binary(a,10)

    assert pos == 5

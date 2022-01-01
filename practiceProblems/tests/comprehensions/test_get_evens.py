
import listAddOns.oneliner.list_even_value as oneliner

def test_evens():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    result = oneliner.listEven(a)


    assert result == [4,16,36,64,100]
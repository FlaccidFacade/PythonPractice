import listAddOns.oneliner.list_ends as oneliner

def test_evens():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    result = oneliner.listEnds(a)


    assert result == [1, 100]
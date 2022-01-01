import listAddOns.palindrome.checker as pal

def test_palindrome():
    isPal = pal.checker("racecar")
    assert isPal == True

    isPal = pal.checker("raceecar")
    assert isPal == True

    isPal = pal.checker("rcr")
    assert isPal == True

    isPal = pal.checker("rr")
    assert isPal == True

    isPal = pal.checker("r")
    assert isPal == False

    isPal = pal.checker("notapalindrome")
    assert isPal == False

    isPal = pal.checker("rascecasr")
    assert isPal == False

    isPal = pal.checker("racheecarh")
    assert isPal == False
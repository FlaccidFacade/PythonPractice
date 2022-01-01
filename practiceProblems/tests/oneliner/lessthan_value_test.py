
import oneliner.list_less_than_value as oneliner

 
def test_list():
    newList = oneliner.listLessThan([1,2,3,4,5,6,7,34,3425,7,3,90],100)
    assert newList == [1,2,3,4,5,6,7,34,7,3,90]
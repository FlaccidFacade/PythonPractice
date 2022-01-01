
import indexing.find_index_sum as indexing

    
def test_find_index_sum_unique():
    pairs = indexing.positionForSum([1,2,3,4,5],5,True)
    assert pairs == [(0,3),(1,2)]
    
def test_find_index_sum():
    pairs = indexing.positionForSum([1,2,3,4,5],5,False)
    assert pairs == [(0,3),(1,2),(2,1),(3,0)]
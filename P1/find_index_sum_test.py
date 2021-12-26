import unittest
import find_index_sum as find

class P1TestCase(unittest.TestCase):
    
    def test_find_index_sum_unique(self):
        pairs = find.positionForSum([1,2,3,4,5],5,True)
        self.assertEquals(pairs, [(0,3),(1,2)])
        
    def test_find_index_sum(self):
        pairs = find.positionForSum([1,2,3,4,5],5,False)
        self.assertEquals(pairs, [(0,3),(1,2),(2,1),(3,0)])
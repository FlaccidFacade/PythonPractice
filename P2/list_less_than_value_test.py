import unittest
import list_less_than_value

class P2TestCase(unittest.TestCase):
    
    def list_test(self):
        newList = list_less_than_value.listLessThan([1,2,3,4,5,6,7,34,3425,7,3,90],100)
        self.assertEqual(newList,[1,2,3,4,5,6,7,34,7,3])
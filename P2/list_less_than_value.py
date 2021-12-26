"""
STATEMENT
Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the user.
"""


def listLessThan(values:list=None, target:int=None) -> list:
    """given a list returns a list with values less than the 
    specified target value

    Args:
        values (list, optional): list to sift through. Defaults to None.
        target (int, optional): the cutoff value to remove. Defaults to None.

    Returns:
        list: the sifted list of values less than the target value
    """
    
    return [x for x in values if x < target]
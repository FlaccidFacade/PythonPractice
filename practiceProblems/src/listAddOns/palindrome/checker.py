

def checker(a:str==None)->bool:
    """checks if a string is a palindrome

    Args:
        a (str, optional): the palindrome in question. Defaults to =None.

    Returns:
        bool: if it is a palindrome or not
    """

    l = len(a)
    if l < 2:
        return False

    for i, val in enumerate(a):
        if val != a[l-1-i]:
            return False


    return True
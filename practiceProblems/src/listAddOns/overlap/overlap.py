""""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates).
 Make sure your program works on two lists of different sizes."""



def overlaps(a:list==None,b:list==None)->list:
    """Creates a list of overlapping values

    Args:
        a (list, optional): first list to use. Defaults to =None.
        b (list, optional): second list to use. Defaults to =None.

    Returns:
        list: overlapping values
    """
    ol = []
    for x in a:
        if x in b and not x in ol:
            ol.append(x)
    
    return ol
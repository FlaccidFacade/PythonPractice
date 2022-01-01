

def listEven(values:list=None) -> list:
    """Creates a list of only the even values

    Args:
        values (list, optional): list to augment. Defaults to None.

    Returns:
        list: even values
    """
    return [x for x in values if x % 2 == 0]

def listEnds(values:list=None) -> list:
    """Creates a list of only the first and last values

    Args:
        values (list, optional): list to augment. Defaults to None.

    Returns:
        list: end values
    """
    return [values[0], values[len(values)-1]]
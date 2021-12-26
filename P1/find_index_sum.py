"""
STATEMENT
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
CLARIFICATIONS
- What happens when there is no solution? Assume solution exists.
- Can the list be empty? No.
- Is the list sorted? Not necessarily.
EXAMPLES
[2, 7, 11, 15], 9 -> [0,1]
"""


def positionForSum(values:list=None, target:int=None, unique:bool=False) -> dict:
    """find the positions of values that sum to the target value

    Args:
        values (list, optional): array of integers used to search in. Defaults to None.
        target (int, optional): the target sum to find. Defaults to None.

    Returns:
        dict: of indices of the two numbers such that they add up to the target.
    """
    
    #create arrays for keeping track of values
    indices = []
    unique_indices = []

    #iterate over values and positions
    for pos,val in enumerate(values):
        #calculate the compliment to search for
        compliment = target - val

        if compliment in values:
            compliment_pos = values.index(compliment)
            
            if unique and not pos in unique_indices:
                unique_indices.append(compliment_pos)
                indices.append((pos,compliment_pos))
            elif not unique:
                indices.append((pos,compliment_pos))

    return indices
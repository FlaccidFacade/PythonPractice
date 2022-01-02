

def iterate(values:list==None, target)-> int:
    for i,val in enumerate(values):
        if val == target:
            return i
    return -1



def binary(values:list==None, target, low:int=None, high:int=None)-> int:
    
    if not low:
        low = 0
    if not high:
        high = len(values) - 1

    if low > high:
        return -1

    midpoint = (low+high) // 2

    if values[midpoint] == target:
        return midpoint
    if values[midpoint] < target:
        return binary(values, target, low=midpoint, high=high)
    else:
        return binary(values, target, low=low, high=midpoint)

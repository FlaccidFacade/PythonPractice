"""Create a program that asks the user for a number and 
then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that 
divides evenly into another number. For example, 13 is a 
divisor of 26 because 26 / 13 has no remainder.)"""



def get(numerator:int==0) -> list:
    """gets the list of divisors for the given numerator

    Args:
        numerator (int, optional): The value we are looking divisors of. Defaults to =0.

    Returns:
        list: The list of divisors found
    """
    l = []
    for i in range(1,numerator+1):
        if numerator % i == 0:
            l.append(i)

    return l
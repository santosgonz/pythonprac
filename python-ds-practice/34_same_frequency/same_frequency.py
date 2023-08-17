def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_1 = str(num1)
    sorted_1 = sorted(str_1)
    str_2 = str(num2)
    sorted_2 = sorted(str_2)
    if sorted_1 == sorted_2:
        return True
    elif sorted_1 != sorted_2:
        return False
        
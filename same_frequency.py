def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    from collections import Counter


    num1_str = str(num1)
    num2_str = str(num2)


    count1 = Counter(num1_str)
    count2 = Counter(num2_str)


    return count1 == count2
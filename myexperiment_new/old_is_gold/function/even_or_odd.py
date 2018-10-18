'''
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''


def lesser_of_two_evens(u1, u2):
    #check first number
    if u1 % 2 == 0 and u2 % 2 == 0:
        if u1 < u2:
            result = u1
        else:
            result = u2
    else:
        if u1 < u2:
            result = u2
        else:
            result = u1

    return result


print(lesser_of_two_evens(2, -57))
'''
best solution
'''


def lesser_of_two_evens1(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens1(2, -57))

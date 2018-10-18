'''
BLACKJACK: Given three integers between 1 and 11, *if their sum is less than or equal to 21, return their sum. 
*If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
*Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
###################################
num =[4,5,6]
numstar=sum(num)

'''


def blackjack(u1, u2, u3):

    if sum((u1, u2, u3)) <= 21:
        return sum((u1, u2, u3))
    else:
        if u1 == 11 or u2 == 11 or u3 == 11:
            return sum((u1, u2, u3)) - 10
        else:
            return "BUST"


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

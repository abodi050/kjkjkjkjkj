def multiply(numbers):
    global total
    for a in numbers:
        total = a * total
    return total


lst = [1, 2, 3, -4]
total = 1
print(multiply(lst))

#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;


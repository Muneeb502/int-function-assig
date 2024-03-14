"""

## Define a function named is_even that takes an integer parameter num and returns True if the number is even, otherwise False.

- Input: is_even(7)
- Output: False
    """
    
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
num = int(input("Enter any number = "))
print(is_even(num))
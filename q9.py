""""
## Create a function named is_prime that takes an integer parameter num and returns True if the number is prime, otherwise False.

- Input: is_prime(7)
- Output: True

"""

def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return True
        else :
            return False


num = int(input("ENTER ANY NUMBER : "))
print(is_prime(num))
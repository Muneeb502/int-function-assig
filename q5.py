"""

## Write a function called factorial that calculates the factorial of a given number n.

- Input: factorial(5)
- Output: 120

"""
def factorial(n):
    sum = 1
    for i in range(1,n):
        sum += sum*i
    return sum 
n = int(input("ENTER ANY NUMBER = "))
print(factorial(n))


"""
1*1 = 1
1*2 = 2
2*3 = 6
6*4 = 120

    """
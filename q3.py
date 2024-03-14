"""## Create a function named power that takes two parameters: base and exponent, and returns base raised to the power of exponent.

- Input: power(2, 3)
- Output: 8
    """
def power(a,x):
    return a**x

num = int(input("enter the base = "))
num2 = int(input("enter the exponent = "))

print(power(num,num2))
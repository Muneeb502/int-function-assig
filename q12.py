"""""
## Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
    
- Expected Output :
- No. of Upper case characters : 3
- No. of Lower case Characters : 12

"""
def upper_and_lower_counter(anysentence):
    count_upper = 0
    count_lower = 0
    for k in anysentence:
        if k.isupper():
            count_upper += 1
        elif k.islower():
            count_lower += 1
    return count_upper, count_lower

anysentence = input("ENTER ANY WORD:")
upper_count, lower_count = upper_and_lower_counter(anysentence)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)


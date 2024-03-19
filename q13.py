""""
## Write a Python function to multiply all the numbers in a list.

- Sample List : (8, 2, 3, -1, 7)
- Expected Output : -336


"""
def multiply_numbers_int_uple(Tupl):
    result = 1
    for i in Tupl:
        result = result*i
    return result
    

tupl = (3,6,9,5,-2,5,-7,4)
print(multiply_numbers_int_uple(tupl))


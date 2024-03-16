""""
## Define a function named reverse_list that takes a list parameter lst and returns a new list with the elements reversed.

- Input: reverse_list([1, 2, 3, 4, 5])
- Output: [5, 4, 3, 2, 1]

"""
def reverse_list(original_list):
    return original_list[::-1]
    
original_list = [ int(i) for i in input("ENTER any numbers for list which is separated by { space }").split(" ")]
print(reverse_list(original_list))
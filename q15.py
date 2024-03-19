""""
## Define a function named square_dict that takes a list of integers as input and returns a dictionary where each key-value pair consists of an element from the input list as the key and its square as the value.

- Input: [1, 2, 3, 4, 5]
- Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
- Note: You can use dictionary comprehension for better practices 


"""
def square_dict(user_list):
    result = {}
    for i in user_list:
        result[i] = i **2
    return result        


user_list = [int(p) for p in input("ENTER ANY NUMBERS FOR LIST = ").split()]
print(square_dict(user_list))
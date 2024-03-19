"""""
## Write a Python function named get_initials that takes a string as input and returns the initials of each word in the string, separated by dots.

- Input: "John Doe"
- Output: "J.D"

"""


def get_initials(name):
    short_nmae = ""
    for j in name:
        if j.isupper():
            short_nmae +=j+"."
    return short_nmae
            
    
name = input("enter any name : ")

print(get_initials(name))
""""
## Write a python function to remove a letter "e" from the string "elephant".

- output = 'lphant' (all 'e' characters are removed)


"""
def removechar(stringname):
    return stringname[1:]
    
stringname = "elephant"
print(removechar(stringname))
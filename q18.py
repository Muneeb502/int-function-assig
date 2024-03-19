"""""

## Write a python function to remove duplicate character from a string.

- Input: 'levels'
- output: 'vs' (l and e are removed since they are repeating characters in the string)


"""
def remove_multiple_char(input_string):
    empyt = set()
    result =""
    for char in input_string:
        if char not in empyt:
            empyt.add(char)
            result += char
    return result


input_string = input("enter any words : ")

print(remove_multiple_char(input_string))

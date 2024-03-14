""""## Create a function named is_palindrome that takes a string parameter text and returns True if the text is a palindrome, otherwise False.

- Input: is_palindrome("radar")
- Output: True

- Note: A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.Example: "radar" is a palindrome because it reads the same forward and backward.
"""
    
    
    
def is_palindrome(txt):
    reversed_txt = txt[::-1]
    if reversed_txt == txt:
        return True
    else:
        return False

txt = input("Enter any word: ")
print(is_palindrome(txt))
""""
## Write a Python program for a given string S which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string.

- Input: Str = HappyNewYear
- Output: HapyNewYr
- Explanation: After removing duplicate characters such as p, e, a, we have string as “HapyNewYr”.


"""
def removing_duplicate(str):
    empty = set()
    result = ""
    for i in str:
        if i not in empty:
            result += i
            empty.add(i)
    return result

str = input("ENTER ANY STRING ")

print(removing_duplicate(str))
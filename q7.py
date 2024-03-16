"""""
## Define a function named unique_elements that takes a list parameter lst and returns a list containing only the unique elements of the input list.
`
- Input: unique_elements([1, 2, 3, 3, 4, 5, 5])
- Output: [1, 2, 3, 4, 5]

"""
def unique_elements(randomlist):
    emptylist = []
    resultlist=[]
    for i in randomlist:
        if i not in emptylist:
            emptylist.append(i)
            resultlist.append(i)
    return resultlist


randomlist = input("ENTER ANY LIST which is separat by { sapce }").split(" ")
print(unique_elements(randomlist))


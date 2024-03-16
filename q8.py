"""""
## Write a function called average that calculates the average of a list of numbers passed as a parameter.

- Input: average([1, 2, 3, 4, 5])
- Output: 3.0

"""

def average(numerlist):
    sum = 0 
    for i in numerlist:
        sum += i
    return sum/len(numerlist)    
    
numerlist = [int(x) for x in input("enter any numbers of lost = ").split(" ")]
print(average(numerlist))

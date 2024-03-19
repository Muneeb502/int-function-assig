""""
## Given a list in Python and provided the positions of the elements, write a fucntion to swap the two elements in the list.

- Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
- Output : [1, 5, 3, 4, 2]

"""
def swapping(numbers,num1,num2):
    
    if num1 and num2 in numbers:
        
        ind1 = numbers.index(num1)
        ind2 = numbers.index(num2)
        
        numbers[ind1] , numbers[ind2] =numbers[ind2] , numbers[ind1]
    return numbers
numbers = [int(r) for r in input("enetr any numbers = ").split()]

num1, num2 = map(int, input("Enter two numbers for swapping: ").split())

print(swapping(numbers,num1,num2))



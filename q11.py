""""
## Write a Python program to print the even numbers from a given list.

- Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Expected Result : [2, 4, 6, 8]

"""
def evennumbers_list(random_number_list):
     empty = []
     for k in random_number_list:
         if k % 2 ==0:
             empty.append(k)
             
     return empty   
random_number_list = [int(j) for j in input("ENTER ANY NUMBERS : ").split(" ")]
print(evennumbers_list(random_number_list))
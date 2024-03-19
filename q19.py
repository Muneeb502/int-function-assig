"""""
## Write a python function to count the frequencies of each character in the given string and stored it in a dictionary format.

- Input: 'listen'
- Output : {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}


"""
def count_frequncy(name_string):
    freq_dicto = {}
    for i in name_string:
        if i  in freq_dicto:
            freq_dicto[i] +=1
            # freq_dicto[i] = 1
        else:
             freq_dicto[i] = 1
          #  freq_dicto[i] +=1
    return freq_dicto
             

name_string = input("ENTER ANY WORDS : ")

print(count_frequncy(name_string))

from random import choice,shuffle
from array import array

def generate_pass(len):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~']

    temp_pass = choice(nums) + choice(upper) + choice(lower) + choice(sym)
    for x in range(len - 4):
        temp_pass = temp_pass + choice(nums + upper + lower + sym)
        temp_pass_list = array('u', temp_pass)
        shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password += x
    return password

len=15 # длина пароля
count=10 # количество паролей
for el in range(count):
    print(generate_pass(len))

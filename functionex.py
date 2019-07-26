# from random import *
# def is_even(num): #function tests if a num is even and returns true
#     if num % 2 == 0: #checks if num is even
#         return True  #returns True if num is even
#     else:
#         return False #returns False is num is odd
#
# even_num = randint(1,300) #generates a random integer and stores it in the even_num variable
# print even_num #prints the random integer
#
# if is_even(even_num) == True:#links the random integer from even_num to if_even, runs through if_even and checks for True
#     print("Even!") #prints Even if True
# else:
#     print("Odd!")#prints Odd if False
#
# -----------------------------------

numbers = [4,5,6,8,10]

def calc_total(list):
    sum = 0
    # for i in range(len(list)):
    for i in list:
        sum = sum + i
    return sum

print (calc_total(numbers))

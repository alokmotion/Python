# Type of Function

# 1. Built-in Function
#2. User-defined Function

# Built-in function  

# 1. abs()  ---> find the absolute value

num = -100
print(abs(num))

# 2. all()

# return value of all() function
#  True : if  all elements in an iterable are true
#  False  : if  any elements in an iterable is false

lst =  [1,2,3,4]
print(all(lst))

lst =  [0,2,3,4]
print(all(lst))
 

# map() -- > map applies a function to all the items in an input_list
# syntax: map(function_to_apply,list_of_inputs)



# normal method 
number = [1, 2, 3, 4,]
# squared =[]



# for num in number:
#     squared.append(num**2)

# print(squared)



# map method


def powerOfTwo(num):
    return num**2

squared = list(map(powerOfTwo,number))
print(squared)


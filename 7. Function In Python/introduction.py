# ''' Function in Python 


# Function is a group of related statements that perform a specific task. 

# Function help break our program into smaller and modular chunks. As our program grows larger and larger, function make it more organized and manageable. 

# It avoids repetition and makes code reusable. 

# Syntax: 
# def function_name(parameters): 
#  """ 
#  Doc String 
#  """ 
#  Statements(s) 
 
 

#  Keyword "def" marks the start of function header 
#  Parameters (arguments) through which we pass vaues to a function. these are optional 1
#  A colon (:) to mark the end of function header 
#  Doc string describe what the function does. this is optional 
# "return" statement to return a value from the function. this is optional1
 
 
 


#  '''


# def print_name(name):
#     '''
#     this is function to print the name 
#     '''
#     print("hello " + str(name))


# # function call  --> Once we have defined a function, we can call it from anywhere

# print_name("alok")



# # Doc string 

# print(print_name.__doc__)


# # Return statement  - 


# def get_sum(lst):
#     """
#     this function returns the sum of all the elements in a list

#     """
#     _sum = 0 # initialize sum 

#     for num in lst:
#         _sum += num
#     return _sum


# s = get_sum([1,2,3,4])
# print(s)


# for looping to understand use python tutor website

# scope of variable
# global_var = "this is global variable "
# def test_life_time():
#     """
#     this function test the life time of a variable

#     """
#     local_var = "this is Local Variable"
#     print(local_var)
#     print(global_var)


# test_life_time()

# print(global_var)
# # print(local_var) # error

#  Pyhton program to print Highest Common Factor(HCF)  of two numbers

def hcf(a,b):

    smaller = b if a> b else a

    hcf = 1
    for i in range(1, smaller+1):
        if (a%i ==0) and (b%i ==0):
            hcf = i
    return hcf

num1 = 97
num2 = 78
print(hcf(num1,num2))




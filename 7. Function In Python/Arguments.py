# # function Arguments


# def greet(name,msg):


#     print("hello {0},{1}" .format(name,msg))

# # call the functiom with arguments

# greet("Alok ", " Good mornig")


# # if we pass one arguments it will thro error

# '''Type of Arguments 

# 1. Default Arguments
# 2. Keyword Arguments 
# 3. Arbitary Arguments -- 
 
#  '''
# #  Default Arguments



# def greet(name,msg="goodnight"):


#     print("hello {0},{1}" .format(name,msg))

# # call the functiom with arguments

# greet("Alok " )#" Good mornig")

# Keyword Arguments

def greet(**kwargs):
    if kwargs:
        print( "hello {0},{1}" .format(kwargs['name'], kwargs['msg']))

greet(name="alok2" ,msg="ji")

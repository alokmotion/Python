'''
TOPIC: BOOLEANS, COMPARISON OPERATORS AND LOGICAL OPERATORS

bool - A boolean is a data type that can have a value of true or false
'''

# isMarried = False

# print(isMarried)

'''

1) <= Smaller than or equal to
2) >= Greater than or equal to
3) < Smaller than
4) > Greater than
5) == Equal to
6) != not equal to

'''
# CODE STRAT
# print(2>2)
# print(4>7)
# print(7<9)
# print(9==9)
# print(9==7)
# CODE END

'''
Logical Operator

1) and Evaluate if both side are true 
2) or Evaluate if atleast one side is true
3) not Inverse a boolean type 

'''
# CODE START

# and

# print(True and True)
# print(True and False)
# print (False and True)
# print(False and False)

# or
# print(True or True)
# print(True or False)
# print (False or True)
# print(False or False)

# not
# print (not True)
# print (not False)

# CODE END


'''
TODO Practice 

Write code to evaluate age, as a teenager. Boy/Girl having age between 12 and 20 is 
considered as teenager.

Store the result in variable and print on screen.

'''
# CODE START
age = 19

isTeenAger = age>=12 and age <=20

print(isTeenAger)


# CODE END

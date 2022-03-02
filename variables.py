'''
Variables are like container that is used to store values.
Storing values are important, because we need to use it later in our code.

NOTE print() is a useful built-in function that displays input value as text in the output.

'''

# CODE START

# num = 2
# num1 = 3
# num2 = -5

# print(num+num1+num2)

# print(num2-num1)

# print(num2-num1)


# CODE END


# RULES FOR NAMING VARIABLES
# 1) Variable name must always start with either _ or any letter a-z, A-Z.
_num2 = 5


# 2) Variable name is case sensitive.
# num3 = 7
# Num3 = 9
# print(num3)
# print(Num3)

# 3) Variable name must not contain space.

# num4 num5 = 4

# 4) Camel case, not mandatory but best practice.
# isgreaterthan
# isGreaterThan


'''
Each value has it's own data type. Data type is important because
each value in programming need to be executed according to their
data type. For example number can be treated as number, which 
means we can perform arithmetic operations on number.

There are two data types for number
1) Integer
2) Float
'''
# CODE START
# number1 = 7
# number2 = 34.5

# print(type(number2))
# print(type(number1))


# CODE END


'''
TODO Practice the variables

There are 5 Students in the class. All students have given their test.
Marks of the students are as follow:
70, 80, 75, 65, 50 respectively.

What is the average result of the class.
NOTE First store the marks of all students in variable, then calculate
it's average store the result of calculated result in variable called
average. print the average.
'''
# CODE START

totalStudentOfClass = 5

stdA=70
stdB=80
stdC=75
stdD=65
stdE=50

avg = (stdA + stdB + stdC + stdD + stdE)/totalStudentOfClass

print(avg)




# CODE END

'''
if statement syntax

if test expresion:
    statement(s)
the program evaluates the test expration and will execute statement(s) only if the text expresssion is True
if the text expresssion is False, the statement(s) is not executed.



'''
# if statement

num = 10
if num>10:
    print("Number is positive")
print("This will print always")


# if...else statement

num = 10
if num >0:
    print("Positive number")
else:
    print("Negative number")
     


# if....elif...else..statements

num = 0

if num> 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# Nested if statement

# We can  have a if ..elif..else statement inside another if..elif...else statement.this is called nesting in computer programming

num = 10.5
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("positive Number")
else:
    print("Negative Number")



#  Pyhton program to find the largest element among three number
num1 = 10
num2 = 200
num3 = 40

if (num1 > num2 ) and (num1>num3):
    largest = num1
elif (num2 >num1) and (num2>num3):
    largest = num2
else:
    largest = num3

print("the largest number is {}" .format(largest))
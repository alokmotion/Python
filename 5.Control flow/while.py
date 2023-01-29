# while loop

'''
syntax: 
while test_expression:
    body of while


    the body of the loop is entered only if the test_expression evaluates to True.
    After one iteration, the test expression is checked again
    the process continues until the test_expression evalutes to False


'''
'''

# find the product of all number present im a list
lst = [10, 20, 30, 40, 50]
product = 1
index = 0

while index < len(lst):
    product *= lst[index]
    index += 1
print("product is: {} ".format(product))


# iterating over the list


numbers = [1,2,3,4,5]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
else:
    print("No item left in the list")

'''

#  Pyhton Program to check given number is prime number or not

num = int(input("Enter a Number : "))

isDivisible = False

i = 2;
while i < num:
    if num % i == 0:
        print("{} is Divisible by {}" .format(num,i))
    i += 1;
if isDivisible:
    print("{} is NOT a Prime Number".format(num))
else:
    print("{} is a prime number ".format(num))


# ------------------------Python string--------------------

# string  
            # string in python are  surrounded by either single quatation mark or double quotation.
            # "hello"




x = "hello world i am alok patel"


# type check

print(type(x))

#check length 

print(len(x))

# check position of character at position 

print(x[6])

# loop through a string 
# loop through the letters in word "bababa"



for y in "banana":
    print(y)

# To check if a certain phrase or character is present in a string, we can use the keyword in.

print("alok" in x)
print("shivam" in x)


# Use it in an if statement: 
# if "yes" 
if "alok" in x :
    print("alok motion classes")

if "amit" in x :
    print("alok motion classes")

# if not present 

if "amit" not in x:
    print ("i am the wold happy man ")


            # -----------------Python - Slicing Strings ---------------------

    #   find range        

chr1 = "baba bhole nath"

print(chr1[2:9])

print(chr1[:10])

print(chr1[10:])

print(chr1[-5:-2])

            # ------------------Python - Modify Strings -------------------

            # Python has a set of built-in methods that you can use on strings.


# upper case 

vax = "   Ram Is Very Nice Person   "

print(vax.upper())

# lowercase

print(vax.lower())

# remove whitespace

print(vax.strip())

# replace string

print(vax.replace("Ram","Shyam"))
print(vax.replace("i","x"))

# split string 

print(vax.split(","))
print(vax.split())



# -------------string Concatenation-------------------
# combine two variable to use + operator
# lest see the example 

man1= "alok motion"
man2= "classes"
 
z = man1+" "+man2

print(z)


# ------------------- Python - Format - Strings---------------------------------------------

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

"""
age = 20
selfintro = "My name is alok, and my age is " + age
print(selfintro)

"""

# but we can combine strings and numbers by using format() method 
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:



Age = 20
SelfIntro = "My name is alok, and my age is {} "
print(SelfIntro.format(Age))


# the format() method takes  unlimited numbers and arguments and are placed into thr respective placeholder


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



# or

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))







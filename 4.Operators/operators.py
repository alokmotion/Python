'''
Operators in Pyhton
Operators are special symbols in Python that carry out arithmetic and logical computation.
the value that operator on is called the operand.

Type : -

Arithmetic Operators
Comparison (Relational) operators
Logical(Boolean) Operators
Bitwise Operators
Assignment Operators
Special Operators


'''

# Arithmetic Operators (+ , - , *, /,%,//,**)

x,y = 10,20

# addition 
print(x+y)
# Subtraction
print(x-y)
# Multiplication
print(x*y)
# division
print(x/y)
# Module division 
print(x%y)
# Floor Division 
print(x//y)
# Exponent
print(x**y)


#  Comparison (Relational) operators  (>,<,==,!=,>=,<=,)
a, b =10, 20
# check a is less then b 
print(a<b)

# check a s greater than b
print(a>b)


# Logical(Boolean) Operators (and or not)
a, b = True , False
# print a and b
print(a and b)
# print a or b
print(a or b)

# print not b
print( not b)

# Bitwise Operators (&, |, ~, ^, >>, <<)
c, d = 10, 4

# bitwise  AND
print(c&d)

# bitwise  OR
print(c|d)

# bitwise  NOT





# Assignment Operators (=, +=, -=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, )

q = 10
q += 10 #add AND
print(q)

# subtract AND 
w = 20
w -= 30
print(w)




# Special Operators
 
# is and is not are the identity operators in pyhton


p = 5
r = 5
print(p is r)
print(p is not r)


# Membership operators --(in and not in)
# they are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

lst = [1,2,3,4]
print (1 in lst)
print (1  not in lst)

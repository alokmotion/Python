#We use the Assignment operator (=) to  assign values to variable
a = 10
b = 5.5
c = "ML"

# Multiple Assignments

a, b, c, = 10, 5.5, "ML"

# Storage Locations
x = 3
print(id(x))
y = 3
print(id(y)) 
y = 2
print(id(y))



# Data Types
# 1. Numbers ---> int , float, complex number(1+2j)
# int 
a = 5
print(a, " is of type", type(a))
a = 2.5
print(a, " is of type", type(a))
a = 1+2j
print(a, " is of type", type(a))
print(isinstance(1+2j, complex))


# 2. Boolean  --> boolean represents the truth values False and True
a = True
print(type(a))

# 3. String 
'''
String is sequence of unicode characters.
we can use single quotes or doubles quotes to represents strings
'''
s = "This is Online AI course"
print(type(s))


# 4. Pyhton List

a = [10, 20.5, "hello"]
print(type(a))
print(a[2])


# Tuple
t = (1,1.5,"ml")
print(type(t))

print(t[1]) #extract particular element

# t[1] = 2.5  #error

# Set
a = {10,20,30,50,}
print(type(a))

s = {10,20,20,30,30,30} # automatically set won't consider duplicate elements
print(s)



# dictionary
d = {'a':"apple",'b':"bat"}
print(type(d))


'''Conversion between DataTypes'''

print(float(5))
print(int(100.5))
print(str(20))


user = "alok"
lines = 100

print("congratulations, " +user+ "!You just wrote " + str(lines) + "line of code")
print("congratulations, " +user+ "!You just wrote " + lines + "line of code") # eror


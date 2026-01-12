# Type casting means converting one data type to another data type in Python.
# Python allows implicit and explicit type casting.

# Implicit Type Casting
# In implicit type casting, Python automatically converts one data type to another without any user intervention.
# For example, when an integer is added to a float, Python automatically converts the integer to

a = 10      # int
b = 2.5     # float
c = a + b   # int → float automatically
print(c)    # 12.5
print(type(c))  # <class 'float'>


# Explicit Type Casting
# In explicit type casting, the user manually converts one data type to another using built-in functions like int(), float(), str(), etc.
x = 5.7     # float 
y = int(x)  # float → int explicitly
print(y)    # 5
print(type(y))  # <class 'int'> a float before performing the operation.



# list(), tuple(), set()
# Convert between collections
list("abc")      # ['a', 'b', 'c']
tuple([1,2,3])   # (1, 2, 3)
set([1,1,2,3])   # {1, 2, 3}


# Why Type Casting is Used?
# Taking user input
# Performing calculations
# Data validation
# Converting API / file data

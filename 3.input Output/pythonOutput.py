# we use print() function to output data to the standard output device
# pyhton output
print("namste duniya")

a = 10

print("the value of a is ", a )
print("the value of a is " + str(a))

# 1st way
a = 10; b=20 #multiple statement in single line.
print("the value of a is {} and b is {}".format(a,b)) #default

# 2nd way

a = 10; b = 20 
print("the value of b is {1} and a is {0}".format(a,b)) # specify position

#3rd way  we can use keyword arguments to formate the string

print("hello {name}, {greeting}".format(name = "Alok" , greeting = "Good Mornig" ))

# we can combine positional argument with keyword arguments
print('the story of {0}, {1}, and {other}' . format('bill','Manfred', other = 'Georg'))
 
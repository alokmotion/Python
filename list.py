# Lists are used to store multiple items in a single variable.
# list are created using square brakets;
# Allow Duplicates



import this


myList = ["apple" , "banana" , "pineapple","orange"]

list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


print(type(myList))
print(type(list2))
print(type(list3))


print(len(list3))
print(len(list2))
print(len(myList))


print(myList)


# A list can contain different data types:

mylist2 = ["abc", 34, True, 40, "male"]

print(mylist2)


mylist3 = list(("alok" , "ram", "shyam", "kavi" , "bihari","ashish"))

print(mylist3)
print(type(mylist3))



# Python - Access List Items

print(mylist3[1])

print(mylist3[-1])
print(mylist3[2:5])

print(mylist3[:3])
print(mylist3[3:])



if "ram" in mylist3:
  print("Yes, 'ram' is in the fruits list")


# Change Item Value

mylist3[2] = "kiran"
print(mylist3)

mylist3[1:4] = ["raj","shihor"]

print(mylist3)



# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:



# loop through a list

# You can loop through the list items by using a for loop:

thisList = ["apple" , "banana","pineapple"]
for x in thisList:
  print(x)

# loop through the index number 

for i in range(len(mylist3)):
  print(mylist3[i])
  
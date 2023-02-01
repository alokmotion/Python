# # List Creation
# empatylist = []
# lst = ["one", "two", "three"]  #list of string
# lst2 = [1,2,3,4,5]  #list of integer
# lst3 = [[1,2],[3,4]] #list of list
# list4 = [1,"rume",24, 1.45,]  # list of different datatypes

# print(list4)

# # List length
# print(len(list4))



# # list Append  # 

# lst.append('five')  #append will add the item at the end
# print(lst) 


# # list Insert   
# # syntax -->  lst.insert(x,y)
# lst.insert(3,'four')   # will add element  y at location x
# print(lst)


# list Remove


# newlst = ["one", "two", "three", "two", "foure"]
# newlst.remove("two") #it will remove first occurence of "two" in given list
# print(newlst) 


# list Append & Extend

# listA = ["hello", "ram", "how", "are"]
# listB = ["you", "?"]
# append
# listA.append(listB)
# print(listA)


# extend -- extend will join the listA with listB
# listA.extend(listB)
# print(listA)


# lsit delete

# del listA[2]

# print(listA)

# pop() method

# listA.pop(3)
# print(listA)


'''  list related keyword in pyhton'''\

# keyword 'in' is used to test if an item is in a list

# listA = ["hello", "ram", "how", "are"]
# if 'are' in listA:
#     print("Yes it is Abilable")

# if 'you' not in listA:
#     print("Yes it is not Abilable")



# ''' List Reverses'''


# listA = ["hello", "ram", "how", "are"]
# listA.reverse()
# print(listA)



''' String split to create a list'''
s = "one,two,three,four,five"
slst = s.split(',')
print(slst)

t = "Welcome to alok motion classes"
tlist = t.split()
print(tlist)



#   ''' list Looping '''

for ele in tlist:
    print(ele)

#  ''' list Comprehension ''' 



squar =  [ i**2 for i in range(10)]
print(squar)
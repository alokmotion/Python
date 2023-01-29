# # pyhton for loop


# # syntax 
 
# #  for element in sequence:
# #     body of for


# # example
# # find the prioduct of all numbers present in list

# lst = [10, 20, 30, 40, 50]
# product = 1
# # iterating over the list

# for ele in lst:
#     product *= ele
# print(product)


# '''Range()'''
# # print range in 10

# for i in range(10):
#     print(i)


# # print range of number from 1 to 20 with step of 2\

# for i in range (1, 20, 2):
#     print(i)


# lst1 = ["satish", "srinu", "murli", "naveen"]

# for index in range(len(lst1)):
#     print(lst1[index])



# python Program to display all prime numbers within an interval

index1 = 10
index2 = 50
print("Prime number between{} and {} are:".format(index1,index2))
for num in range (index1,index2):
    if num>1:
        isDivisible = False;
        for index in range(2,num):
            if num%index ==0:
                isDivisible = True
        if not isDivisible:
            print(num)

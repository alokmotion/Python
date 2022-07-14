# list1 = [["alok",2] , ["amit",3] , ["ashish",10] ,["abhishek",20]]

# for item,lollypop in list1:
#     print(item , " and lollypop is" , lollypop)



listquize = ["alok ", 26, "hello" , "apple" , 2 ,6,5,8,"radha"]

for item in listquize:
    if str(item).isnumeric() and item>6:
        print(item)
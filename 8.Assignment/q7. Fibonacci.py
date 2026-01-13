
# Agar tum value limit chahte ho → current approach sahi hai
# a = 0
# b = 1

# c = 0
# while(c <= 20):
#     print(a ," \n")

#     c = a+b
#     a = b
#     b = c

# Agar tum number of terms chahte ho → neeche wali approach sahi hai
a = 0
b = 1
n = int(input("Enter number of terms: "))
count = 0
while(count < n):
    print(a, "\n")
    c = a + b
    a = b
    b = c
    count += 1  

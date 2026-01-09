# Immutability : Once created, a tuple cannot be modified.


firstTuple = (1,)

# note : this is single element tuple so we should have to add comana in the last otherwise this will become integer


# print(type(firstTuple))


# secondTuple = (1, 2, 5,5 , "ram")

# Without Parentheses (Tuple Packing)
t = 1, 2, 3

# print(type(seconTuple))


# 3. Accessing Tuple Elements
# print(t[2])


# Slicing

# print(t[0:2])   # (10, 20)



# But mutable objects inside a tuple CAN change:
# t = (1, [2, 3])
# t[1].append(4)
# print(t)  # (1, [2, 3, 4])


print(3 in t)
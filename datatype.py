# pyhton has following bulit in data type 

'''
1. text -
                 str
2. numeric type -
                -> int
                -> float
                -> complex

3.Sequence type - 
                --> list                
                --> tuple
                --> range
                                
4.Mapping Type - 
                --> dict


5.Set type  - 
            --> set
            --> frozenset

6. Boolean Type - 
            --> bool

7. Binary Type -
            --> bytes                        
            --> bytearray
            --> memoryview

8.None Type -    
                --> NoneType        


How to know the type of data 

ans - 


x = 4
print (type (x))


'''

# str   ____> x = "Hello World"	str 

StrType = "hello world"

# note when we stor the value in str then complesary inverted comma (''str'')

print(type(StrType))

IntType = 20

# note in this variable store the integer number

print (type(IntType))

FloatTpye = 10.5

# in this data type store  the  decimal value 

print(type(FloatTpye))

ComplexType = 3j
# in this data type we store imajanary number

print(type(ComplexType))

ListType = ["apple ", "banana", "charry"]

print(type(ListType))

TupleType = ("ram","shyam","alok")

print(type(TupleType))

RangeType= range(6)
print(type(RangeType))






















# print(len(ListType))

# ListType1 = ["abc", 34, True, 40, "male"]
# print(ListType1)

# ListType2 = list(("ram","shyam","ravi"))
# print(ListType2)


# import random

# print (random.randrange (1,20))

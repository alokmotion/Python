# Calculator Program

'''
Take User Opertaions : 
Addition = 1
Subtraction = 2
Multiplication = 3
Division = 4


Take input size from user:

Retrun Oputration Result based on user input
'''
import numbers


AirthmaticOperation =  int(input("Select an operation:\nAddition = 1\nSubtraction = 2\nMultiplication = 3\nDivision = 4\n"))
inputSize = int(input("Eneter the size of input "))

class Calculator:
    def __init__(self, AirthmaticOperation, inputSize):
        self.AirthmaticOperation = AirthmaticOperation
        self.inputSize = inputSize

    def selectOperation(self):
        if self.AirthmaticOperation == 1 : return self.add()
        elif self.AirthmaticOperation == 2 : return self.sub()
        elif self.AirthmaticOperation == 3 : return self.multi()
        elif self.AirthmaticOperation == 4 : return self.div() 
        else : print("Exit Program : Crl+C")

    def userInput(self):
        userinput = []
        for i in range (self.inputSize):
            value = int(input(f"Enter the value {i + 1}: "))
            userinput.append(value)
        return userinput
    
    
    def add(self):
        print("Performing Addition")
        numbers = self.userInput()
        result = 0
        for i in numbers:
            result += i
        return result

    def sub(self):
        print("Performing Subtraction")
        numbers = self.userInput()
        result = numbers[0]
        for i in numbers[1:]:
            result -= i
        return result


    def multi(self):
        print("Performing Multiplication")
        numbers = self.userInput()
        result = 1
        for i in numbers:
            result *= i
        return result


    def div(self):
        print("Performing Division")
        numbers = self.userInput()
        result = numbers[0]  
        for i in numbers[1:]:
            if i == 0:  
                return "Cannot divide by zero!"
        result /= i 
        return result



calc = Calculator(AirthmaticOperation, inputSize)
result = calc.selectOperation() 

if result is not None:
    print(f"Result: {result}")
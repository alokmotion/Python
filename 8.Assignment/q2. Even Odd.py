userValue =  int(input("Enter Value to check the value is even or odd if this value is even you will get True and if the value is odd you will get false :"))

class EvenOddChecker:
    def __init__(self, userValue):
        self.userValue = userValue

    def performAction(self):
        if (self.userValue % 2  == 0):
            return True
        else:
            return False
        


obj1 = EvenOddChecker(userValue)

print(obj1.performAction())
        

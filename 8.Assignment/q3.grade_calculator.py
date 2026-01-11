

def validateMarks():
    while True:
        try:
            marks =  int(input("Enter your marks: "))
            if(0 <= marks <= 100): return marks
            else: print("Enter viled Marsk")
        except ValueError:
            print("Invalid input. Please enter numeric value for marks.")


class KnowYourGrade:
    def __init__(self,marks):
        self.marks = marks

   
    def calculateGrade(self):
        if(90 <= self.marks <= 100):  
            return "A+"
        elif(80 <= self.marks < 90): 
            return "A"
        elif(70 <= self.marks < 80):  
            return "B"
        elif(60 <= self.marks < 70):  
            return "C"
        elif(50 <= self.marks < 60): 
            return "D"
        else:
            return "Fail"


obj1 =  KnowYourGrade(validateMarks())
print(f"Your Grade is {obj1.calculateGrade()}")
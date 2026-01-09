class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name 
        self.salary = salary

    def EmpDetails(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}"


class Department(Employee):
    def __init__(self, dptId , dptName, id, name, salary):
        super().__init__(id, name, salary)
        self.dptId = dptId
        self.dptName = dptName


    def dptDetails(self):
        emp_details = super().EmpDetails()
        return f"{emp_details}, Department ID: {self.dptId}, Department Name: {self.dptName}"



obj1 = Department(101, "HR", 1, "Alice", 50000)
print(obj1.dptDetails())
'''
Docstring for 8.Assignment.q5.bus_fare_calculator
Requirement:
Write a Python program to calculate bus/railway ticket fare by taking start and end destinations from the user, validating the input, computing the absolute distance between stops, and displaying the total fare based on a per-kilometer rate using a class-based approach.

'''


print("Welcome to Alok Travels")

baseTicketPrice = 10

start = input("Please Enter the Start Destination: ").casefold()
end = input("Please Enter the End Destination: ").casefold()

route = {
    "railway": 0,
    "teenpatti": 10,
    "ranital": 20,
    "adhartal": 30
}

class GetBusTicketPrice:
    def __init__(self, startDestination, endDestination):
        self.startDestination = startDestination
        self.endDestination = endDestination

    def calcPrice(self):
        if self.startDestination not in route or self.endDestination not in route:
            return "Invalid Destinations"

        totalDistanceCovered = abs(
            route[self.startDestination] - route[self.endDestination]
        )
        finalFare = totalDistanceCovered * baseTicketPrice
        return finalFare

obj = GetBusTicketPrice(start, end)
print("Total Fare:", obj.calcPrice())



'''

📝 Python Assignment Questions
Topic: Bus / Railway Fare Calculation System

User se start destination aur end destination input lene ka program likhiye.

Case-insensitive input handle karne ke liye kaunsa string method use karenge?

Stations aur unki distance store karne ke liye kaunsi data structure use hogi?

Start aur end destination valid hain ya nahi, kaise check karenge?

Start aur end ke beech total distance kaise calculate karenge?

Distance calculation mein abs() function ka use kyun hota hai?

Per-kilometer price ke basis par total fare calculate karne ka logic likhiye.

Ek class banaiye jo fare calculation handle kare.

Class ke constructor (__init__) ka role kya hota hai?

Fare calculate karne ke liye ek method define kijiye.

Agar user invalid destination enter kare to program ka kya behavior hona chahiye?

Start aur end destination same ho to fare kya hona chahiye?

Program ko aise design kijiye ki naye stations easily add kiye ja sakें.

Dictionary mein stored values string rakhne par kaunsi problem aati hai?

Casefold aur lower method mein kya difference hai?

Negative fare kyun nahi aana chahiye? Explain with logic.

Program ko user-friendly banane ke liye kaunse validation add karoge?

File ka meaningful naam dena kyun important hota hai?

Code ko modular banane ka kya fayda hai?

Real-life railway system ka fare logic is program se kaise match karta hai?



'''
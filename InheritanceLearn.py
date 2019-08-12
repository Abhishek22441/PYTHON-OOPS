class Vehicle:
    def __init__(self, driver, wheels, seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats


class Cab(Vehicle):
    pass


cab_1 = Cab('Sandy', 4, 2)
print(cab_1.driver)

'''How to change class variable of subclass Vehicle'''


class Vehicle:
    # class Variable
    minimumrate = 50

    def __init__(self, driver, wheels, seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats


class Cab(Vehicle):
    minimumrate = 75


print(Vehicle.minimumrate)
print(Cab.minimumrate)

"""How to have child class with more parameters than our parent class
   In this example, we have two classes Cab and Bus which have many 
   attributes which are similar but there are a few which are unique to class
  To solve this, we have created a parent class named Vehicle which contains common attributes and method.
  
"""


class Vehicle:
    minimumrate = 50

    def __init__(self, driver, wheels, seats, kms, bill):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats
        self.running = kms
        self.bill = bill

    def rateperkm(self):
        return self.bill / self.running


class Cab(Vehicle):
    minimumrate = 75

    def __init__(self, driver, wheels, seats, kms, bill, cabtype):
        Vehicle.__init__(self, driver, wheels, seats, kms, bill)
        self.category = cabtype


"""We can replace this command Vehicle.__init__(self,driver,wheels,seats,kms,bill)
 with 
super().__init__(driver,wheels,seats,kms,bill).
super() is used to refer the parent attributes and methods."""


class Bus(Vehicle):
    minimumrate = 25

    def __init__(self, driver, wheels, seats, kms, bill, color):
        Vehicle.__init__(self, driver, wheels, seats, kms, bill)
        self.color = color


cab_1 = Cab('Prateek', 4, 3, 50, 700, 'SUV')
print(cab_1.category)
print(cab_1.rateperkm())

bus_1 = Bus('Dave', 4, 10, 50, 400, 'green')
print(bus_1.color)
print(bus_1.rateperkm())

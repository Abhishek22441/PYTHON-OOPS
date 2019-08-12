"""What is __str__?"""

"""It is used to produce readable representation of the object."""


class Vehicle:
    def __init__(self, driver, wheels, seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats


veh_1 = Vehicle("Sandy", 4, 2)
print(veh_1)

"""<__main__.Vehicle object at 0x7f06737ee908>"""


class Vehicle:
    def __init__(self, driver, wheels, seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats

    def __str__(self):
        return "Driver Name : " + self.driver + " ; " + "Number of seats in cab : " + str(self.noofseats)


veh_1 = Vehicle("Sandy", 4, 2)
print(veh_1)

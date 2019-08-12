class Flat:
    def __init__(self):
        self.type = "premium"
        # Here __bhk is private methods
        self.__bhk = "3 BHK"


flat_1 = Flat()
print(flat_1.type)
# print(flat_1.__bhk) AttributeError: 'Flat' object has no attribute '__bhk'
"""In the above program, type is a public attribute and bhk is a private attribute which can't be accessed outside class."""

"""Getters and Setters"""

"""They are used for retrieving and updating value of a variable. 
Setter is a method that updates value of a variable.
 Getter is a method that reads value of a variable."""


class Vehicle:
    def __init__(self, driver_firstname, driver_lastname):
        self.fdriver = driver_firstname
        self.ldriver = driver_lastname
        self.email = self.fdriver + '.' + self.ldriver + '@uber.com'


veh_1 = Vehicle("Sandy", "Stewart")

print(veh_1.email)

veh_1.fdriver = 'Tom'
print(veh_1.email)

"""Here we are updating driver's first name but it does not have an impact on 
email address which is a combination of first and last name."""


class Vehicle:
    def __init__(self, driver_firstname, driver_lastname):
        self.fdriver = driver_firstname
        self.ldriver = driver_lastname

    @property
    def email(self):
        return self.fdriver + '.' + self.ldriver + '@uber.com'


veh_1 = Vehicle("Sandy", "Stewart")
veh_1.fdriver = 'Tom'
print(veh_1.email)

"""How to update first and last name automatically by changing email address"""


class Vehicle:
    def __init__(self, driver_firstname, driver_lastname):
        self.fdriver = driver_firstname
        self.ldriver = driver_lastname

    @property
    def email(self):
        return self.fdriver + '.' + self.ldriver + '@uber.com'

    @email.setter
    def email(self, address):
        first = address[:address.find('.')]
        last = address[address.find('.') + 1:address.find('@')]
        self.fdriver = first
        self.ldriver = last


veh_1 = Vehicle("Sandy", "Stewart")
veh_1.email = 'deep.bhalla@uber.com'
print(veh_1.fdriver)
print(veh_1.ldriver)


"""Validation"""

"""In real world, getters & setters are mainly used for including validation logic. 
In the example below, we are creating donation class with amount attribute. 
Amount must lie between 10 and 1,000,000. If user enters less than 10, it should be set as 10. 
Similarly, if user tries to enter a value greater than 1 million, it should be capped to 1 million only."""


class donation:
    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 10:
            self.__amount = 10
        elif amount > 1000000:
            self.__amount = 1000000
        else:
            self.__amount = amount

charity = donation(5)
print(charity.amount)

charity = donation(1000000000000)
print(charity.amount)
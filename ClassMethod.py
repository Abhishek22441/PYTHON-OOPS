'''Class takes cls as the first argument.
cls refers to class.
To access a class variable within a method,
we use the @classmethod decorator, and pass the class to the method'''


class Cab:
    # Initialise variables for first iteration
    numberofcabs = 0
    numofpassengers = 0

    def __init__(self, driver, kms, places, pay, passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofcabs = Cab.numberofcabs + 1
        Cab.numofpassengers = Cab.numofpassengers + passengers

    # Returns price of cab fare per km
    def rateperkm(self):
        return self.bill / self.running

    # Returns number of cabs running
    @classmethod
    def noofcabs(cls):
        return cls.numberofcabs

    # Returns average number of passengers travelling in a cab
    @classmethod
    def noofpassengers(cls):
        return int(cls.numofpassengers / cls.numberofcabs)


firstcab = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 3)
secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
thirdcab = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)


print(firstcab.driver)

print(firstcab.noofcabs())
print(thirdcab.numofpassengers)


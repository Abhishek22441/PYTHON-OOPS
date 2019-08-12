"""Method Overriding"""

"""Method overriding allows us to have a method in the child class with the same name as in the parent class
 but the definition of the child class method is different from parent class method."""


class Vehicle:
    def message(self):
        print("Parent class method")


class Cab(Vehicle):
    def message(self):
        print("Child Cab class method")


class Bus(Vehicle):
    def message(self):
        print("Child Bus class method")


x = Vehicle()
x.message()
# Parent class method

y = Cab()
y.message()
# Child Cab class method

z = Bus()
z.message()
# Child Bus class method

"""As you can see the output shown above, children classes override the parent class method."""

""""""

"""Method Overloading"""

"""If a class has multiple methods having same name but different in parameters, it is known as Method Overloading."""


class Human:

    def sayHello(self, name=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create instance
obj = Human()

# Call the method
print(obj.sayHello())

# Call the method with a parameter
print(obj.sayHello('Guido'))

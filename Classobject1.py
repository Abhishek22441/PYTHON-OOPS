class car:
    # attributes
    year = 2016  # car model's year
    mpg = 20  # mileage
    speed = 100  # current speed

    # methods
    def accelerate(self):
        return car.speed + 20

    def brake(self):
        return car.speed - 50


car1 = car()
print(car1.accelerate())

print(car1.brake())

print(car1.mpg)
print(car1.speed)

class Test:
    a = 10

    def __init__(self):
        Test.b = 20

    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50

    @staticmethod
    def m3():
        Test.f = 60


print(Test.a)
# print(Test.m1())
# print(Test.b)

print(Test.m3())


t = Test()
print(t.b)
t.m1()
print(t.c)
t.m2()
print(t.d)
print(t.e)
t.m3()
print(t.f)
print(Test.f)
Test.m3()


class Cab:

    @staticmethod
    def billvalidation(pay):
        return int(pay) > 0


print(Cab.billvalidation(0.2))


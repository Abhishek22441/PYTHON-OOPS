class Company:
    # attributes
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    no_of_employees = 100

    # method
    def productivity(self):
        return Company.revenue / Company.no_of_employees


Company1 = Company()
print(Company1.revenue)
print(Company1.no_of_employees)
print(Company1.productivity())

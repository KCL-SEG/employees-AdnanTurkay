"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, salary=0, hours=None, hourly_rate=None, contracts=None, contract_rate=None, bonus=0):
        self.name = name
        self.salary = salary + bonus
        self.hours = hours
        self.hourly_rate = hourly_rate
        self.contracts = contracts
        self.contract_rate = contract_rate

    def get_pay(self):
        self.calculate_salary()
        return self.salary

    def __str__(self):
        return self.name

    def calculate_salary(self):
        if self.hours is not None:
            self.salary += self.hours * self.hourly_rate
        if self.contracts is not None:
            self.salary += self.contracts * self.contract_rate


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, None, None, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, None, None, None, None, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, None, None, 600)

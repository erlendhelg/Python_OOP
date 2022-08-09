

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    @property
    def email(self):
        return "{}.{}@email.com".format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.fname = first
        self.lname = last


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        

emp_1 = Employee("King", "Kong", 70000)
emp_2 = Employee("luke", "skywalker", 10000000)
emp_1.raise_amount = float(1.5)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# print(emp_1.__dict__)
# print(emp_2 .__dict__)
# print(Employee.num_of_emps)
print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = "Richard Richardson"
print(emp_1.fullname)
print(emp_1.email)

print(emp_1.fname)

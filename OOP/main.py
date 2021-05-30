class Employee:
    raise_amount = 1.04
    number_of_employee = 0

    def __init__(self, name, surname, salary):
        self.__name = name
        self.__surname = surname
        self.__salary = salary

        Employee.number_of_employee += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @surname.deleter
    def surname(self):
        del self.__surname

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)

    def get_email(self):
        return '{}.{}@company.com'.format(self.name, self.surname)

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_amount)

    # str() and repr() both are used to get a string representation of object. str() is used for creating output for
    # end user while repr() is mainly used for debugging and development.repr’s goal is to be unambiguous and str’s
    # is to be readable.
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.name, self.surname, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.get_full_name(), self.get_email())

    # Add operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.get_full_name())

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # If a method does not access any class variable. the method should be defined as static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, surname, pay, prog_lang):
        super().__init__(first, surname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, surname, pay, employees = None):
        super().__init__(first, surname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print(emp.get_full_name())


emp1 = Employee('John', 'Smith', 30000)

dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'Employee', 60000, 'Java')

print('----------------------')
print('Overloading len function to get full name lenght')
print(len(dev1))


print('----------------------')
print('Combined Salary of two develoeprs ' + str(dev1 + dev2))

print('----------------------')

print(emp1.__str__())
print(emp1.__repr__())

print('----------------------')

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])
print(mgr1.get_full_name())
print(mgr1.get_email())
print(mgr1.print_employee())

print('----------------------')

mgr1.add_employee(dev2)
print(mgr1.get_full_name())
print(mgr1.get_email())
print(mgr1.print_employee())

print('----------------------')

mgr1.remove_employee(dev1)
print(mgr1.get_full_name())
print(mgr1.get_email())
print(mgr1.print_employee())

print('----------------------')

print(dev1.get_email())
print(dev1.salary)
print(dev1.prog_lang)

print('----------------------')
dev1.apply_raise()

print(dev1.get_email())
print(dev1.salary)
print(dev1.prog_lang)

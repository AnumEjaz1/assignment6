class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable (convention)
        self.__ssn = ssn          # Private variable (name mangling)

# Create an object of Employee
emp = Employee("Alice", 50000, "123-45-6789")

# Access public variable
print("Public variable (name):", emp.name)

# Access protected variable (possible but discouraged)
print("Protected variable (_salary):", emp._salary)

# Access private variable (will cause error if accessed directly)
try:
    print("Private variable (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable __ssn:", e)

# Access private variable using name mangling (not recommended but possible)
print("Private variable using name mangling (_Employee__ssn):", emp._Employee__ssn)

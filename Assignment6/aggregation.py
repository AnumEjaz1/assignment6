class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: Department holds a reference to Employee

    def show_department(self):
        print(f"Department: {self.name}")
        self.employee.display_info()

# Example usage
emp = Employee("Alice", "Software Engineer")  # Employee created independently
dept = Department("IT", emp)                   # Department aggregates Employee

dept.show_department()

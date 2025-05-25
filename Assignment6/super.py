class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)   # Call base class constructor to set name
        self.subject = subject

# Create an instance of Teacher
teacher = Teacher("Mr. Khan", "Mathematics")

# Access attributes
print("Teacher Name:", teacher.name)
print("Subject:", teacher.subject)

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add greet method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Alice")
print(p.greet())  # Output: Hello from Decorator!


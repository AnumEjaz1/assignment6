# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18 years old.")
    else:
        print("Age is valid.")

# Testing with try-except
try:
    check_age(16)  # This will raise the exception
except InvalidAgeError as e:
    print(f"Caught an error: {e}")

try:
    check_age(21)  # This will pass
except InvalidAgeError as e:
    print(f"Caught an error: {e}")

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


# Create an instance with factor 5
mul = Multiplier(5)

# Check if the object is callable
print(callable(mul))  # Output: True

# Call the object like a function
result = mul(10)
print(result)  # Output: 50

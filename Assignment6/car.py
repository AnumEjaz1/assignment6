class Car:
    # Public variable
    brand = ""

    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")

# Instantiate the Car class
my_car = Car()

# Access and set the public variable
my_car.brand = "Hilex"

# Access the public method
my_car.start()

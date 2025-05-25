class Engine:
    def start_engine(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine object
    
    def start_car(self):
        print("Car is ready to start.")
        self.engine.start_engine()  # Access method of Engine class

# Example usage
my_engine = Engine()
my_car = Car(my_engine)
my_car.start_car()

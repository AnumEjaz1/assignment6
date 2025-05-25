class Logger:
    def __init__(self):
        print("🟢 Logger object has been created.")

    def __del__(self):
        print("🔴 Logger object has been destroyed.")

# Create an object
log = Logger()

# Optionally delete the object manually to see the destructor
del log

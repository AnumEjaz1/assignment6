class Counter:
    # Class variable to keep track of the number of objects created
    count = 0

    def __init__(self):
        # Increment the count every time a new object is created
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Class method to display the total number of objects
        print(f"Total objects created: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.show_count()
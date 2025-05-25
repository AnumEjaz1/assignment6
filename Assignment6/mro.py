class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")

class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C):
    pass

# Create an object of class D
d = D()
d.show()

# To explicitly see the Method Resolution Order
print("Method Resolution Order:", [cls.__name__ for cls in D.__mro__])

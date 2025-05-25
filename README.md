

# Python OOP & Programming Assignments - README

This repository contains **21 Python programming assignments** focused on core object-oriented programming concepts, encryption, data handling, decorators, exceptions, iterators, and more. Each assignment demonstrates important Python principles with example code snippets and explanations.

---

## Assignments Summary

### 1. **Secure Data Encryption System with Streamlit**

* In-memory encrypted data storage with passkey authentication.
* Uses Fernet symmetric encryption.
* Streamlit UI with multi-page navigation and login after failed attempts.

---

### 2. **Counter Class Tracking Number of Instances**

* Class variable tracks how many `Counter` objects created.
* Class method displays the current count.

---

### 3. **Car Class with Public Variable and Method**

* Public variable `brand`.
* Public method `start()`.
* Accessed from outside the class.

---

### 4. **Bank Class with Class Variable and Method**

* Class variable `bank_name`.
* Class method `change_bank_name(cls, name)` changes bank name globally for all instances.

---

### 5. **MathUtils Class with Static Method**

* Static method `add(a, b)` returns the sum.
* No use of instance or class variables.

---

### 6. **Logger Class with Constructor & Destructor Messages**

* Prints a message when object is created.
* Prints another message when object is destroyed.

---

### 7. **Employee Class with Public, Protected, and Private Variables**

* Public variable `name`.
* Protected variable `_salary`.
* Private variable `__ssn`.
* Demonstrates access restrictions and name mangling.

---

### 8. **Person and Teacher Classes with Inheritance and super()**

* `Person` constructor sets `name`.
* `Teacher` inherits from `Person`, adds `subject`.
* Uses `super()` to call base class constructor.

---

### 9. **Abstract Base Class Shape and Rectangle Implementation**

* Abstract class `Shape` with abstract method `area()`.
* `Rectangle` implements `area()`.

---

### 10. **Dog Class with Instance Variables and Method**

* Instance variables: `name`, `breed`.
* Method `bark()` prints a message with dog's name.

---

### 11. **Book Class with Class Variable and Class Method**

* Class variable `total_books`.
* Class method `increment_book_count()` to increase count.

---

### 12. **TemperatureConverter Class with Static Method**

* Static method `celsius_to_fahrenheit(c)` converts Celsius to Fahrenheit.

---

### 13. **Composition: Engine and Car Classes**

* `Car` class initialized with an `Engine` object.
* `Car` accesses `Engine` methods via composition.

---

### 14. **Aggregation: Department and Employee Classes**

* `Department` stores reference to an independent `Employee` object.
* Demonstrates aggregation (has-a relationship).

---

### 15. **Multiple Inheritance and Method Resolution Order (MRO)**

* Classes `A`, `B`, `C`, `D` where `B` and `C` inherit from `A`.
* `D` inherits from both `B` and `C`.
* Calls method `show()` from `D` to observe MRO.

---

### 16. **Decorator Function `log_function_call`**

* Prints "Function is being called" before executing a function.
* Applied to `say_hello()` function.

---

### 17. **Class Decorator `add_greeting`**

* Adds method `greet()` returning "Hello from Decorator!" to decorated classes.
* Applied to class `Person`.

---

### 18. **Product Class Using Property Decorators**

* Private attribute `_price`.
* Getter, setter, deleter with `@property`, `@price.setter`, `@price.deleter`.

---

### 19. **Multiplier Class with `__call__` Method**

* Sets a multiplication factor on initialization.
* `__call__` multiplies input by factor.
* Tested with `callable()` and function-like call.

---

### 20. **Custom Exception `InvalidAgeError`**

* Raises `InvalidAgeError` if age < 18 in function `check_age(age)`.
* Handled via `try...except`.

---

### 21. **Countdown Iterator Class**

* Iterable `Countdown` class counts down from a start number to zero.
* Implements `__iter__()` and `__next__()`.

---

## How to Use

* Each assignment is implemented as a standalone Python class or script.
* Run each file independently using Python 3.x.
* Modify examples to experiment with OOP concepts and functionality.

---

## Requirements

* Python 3.6+
* For assignment #1 (encryption + Streamlit):

  * Install `streamlit` and `cryptography` packages:

  ```bash
  pip install streamlit cryptography
  ```

---



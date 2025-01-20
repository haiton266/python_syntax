Refer more from: https://www.geeksforgeeks.org/python-oops-concepts/

### 1. **OOPs Concepts in Python**
OOP (Object-Oriented Programming) is a paradigm that organizes software design around objects, which are instances of classes. Python is an object-oriented language, and its OOP principles include:

1. **Class and Object**: The blueprint (class) and the instance (object).
2. **Polymorphism**: Same interface, different implementations.
3. **Encapsulation**: Bundling data with methods that operate on the data.
4. **Inheritance**: Reusing code by deriving new classes from existing ones.
5. **Abstraction**: Hiding implementation details and showing only the essential features.

---

### 2. **Class in Python**
A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.

#### Syntax:
```python
class ClassName:
    # Class attribute
    class_variable = "Class Variable"

    # Constructor
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Method
    def method_name(self):
        return f"Instance Variable: {self.instance_variable}"
```

#### Example:
```python
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, color):
        self.brand = brand  # Instance attribute
        self.color = color  # Instance attribute

    def start_engine(self):
        return f"{self.brand} engine started!"
```

---

### 3. **Objects in Python**
An **object** is an instance of a class. It represents a specific implementation of the blueprint provided by the class.

#### Example:
```python
# Create objects
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")

# Access attributes and methods
print(car1.start_engine())  # Tesla engine started!
print(car2.color)           # Blue
```

---

### 4. **Polymorphism in Python**
**Polymorphism** allows different classes to use the same method name while providing distinct functionality.

#### Example 1: Function Polymorphism
```python
print(len("Hello"))  # 5 (length of string)
print(len([1, 2, 3]))  # 3 (length of list)
```

#### Example 2: Method Overriding (Runtime Polymorphism)
```python
class Bird:
    def fly(self):
        return "Birds can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly."

bird = Bird()
penguin = Penguin()

print(bird.fly())  # Birds can fly.
print(penguin.fly())  # Penguins can't fly.
```

---

### 5. **Encapsulation in Python**
**Encapsulation** is the concept of restricting access to certain details of an object and exposing only necessary parts. This is achieved using access modifiers:
- **Public**: Accessible anywhere.
- **Protected**: Prefixed with a single underscore `_`, intended for internal use.
- **Private**: Prefixed with double underscores `__`, not accessible directly outside the class.

#### Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

---

### 6. **Inheritance in Python**
**Inheritance** allows a class (child) to acquire properties and methods of another class (parent).

#### Types of Inheritance:
- **Single Inheritance**: One parent, one child.
- **Multiple Inheritance**: One child, multiple parents.
- **Multilevel Inheritance**: Chain of inheritance.
- **Hierarchical Inheritance**: Multiple children from one parent.

#### Example: Single Inheritance
```python
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    def greet(self):
        return "Hello from Child!"

child = Child()
print(child.greet())  # Hello from Child!
```

---

### 7. **Data Abstraction in Python**
**Abstraction** involves hiding complex implementation details and showing only the necessary functionality. In Python, this is achieved using abstract base classes (ABCs) from the `abc` module.

#### Example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rect = Rectangle(4, 5)
print(rect.area())  # 20
print(rect.perimeter())  # 18
```

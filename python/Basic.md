 **dPython fundamentals** 
---

## 🟢 1. Basic Syntax
- Python uses **indentation** (spaces) to define code blocks.
```python
print("Hello World")   # prints text
```

---

## 🟢 2. Variables & Data Types
- Variables store values.  
- Common types: `int`, `float`, `str`, `bool`.
```python
x = 10          # integer
pi = 3.14       # float
name = "Uttam"  # string
flag = True     # boolean
```

---

## 🟢 3. Operators
- Perform calculations or comparisons.
```python
a, b = 5, 2
print(a + b)   # 7
print(a - b)   # 3
print(a * b)   # 10
print(a / b)   # 2.5
print(a % b)   # 1
print(a ** b)  # 25 (power)
```

---

## 🟢 4. Input & Output
- Get user input and display output.
```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

## 🟢 5. Control Flow (Decision Making)
```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 🟢 6. Loops
- Repeat tasks.
```python
# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 🟢 7. Functions
- Reusable blocks of code.
```python
def greet(name):
    return f"Hello {name}"

print(greet("Arun"))
```

---

## 🟢 8. Data Structures
- **List** → ordered, mutable.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits[0])   # apple
```

- **Tuple** → ordered, immutable.
```python
coords = (10, 20)
```

- **Set** → unordered, unique values.
```python
nums = {1, 2, 3, 3}
print(nums)   # {1, 2, 3}
```

- **Dictionary** → key-value pairs.
```python
student = {"name": "Anurudh", "city": "Delhi"}
print(student["name"])
```

---

## 🟢 9. Error Handling
- Prevent crashes with `try/except`.
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 🟢 10. Classes (OOP Basics)
- Bundle data + behavior.
```python
class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        print(f"My name is {self.name} from {self.city}")

s1 = Student("Abhi", "Pune")
s1.introduce()
```

---

## ✅ Big Picture
- **Procedural Python** → variables, loops, functions.  
- **OOP Python** → classes, objects, methods.  
- These fundamentals are the **foundation for apps, databases, and frameworks** like Flask/Django.

---

Would you like me to build you a **step‑by‑step practice roadmap** (Day 1: variables, Day 2: loops, Day 3: functions, etc.) so you can learn Python in a structured way without feeling overwhelmed?
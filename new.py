# # # # # # a = 10
# # # # # # b = 5
# # # # # # sum_result = a * b
# # # # # # print("Sum:", sum_result)


# # # # # # name = input("Enter your name: ")
# # # # # # print("Welcome,", name)


# # # # # # number = int(input("Enter a number: "))
# # # # # # if number % 2 == 0:
# # # # # #     print("Even number")
# # # # # # else:
# # # # # #     print("Odd number")



# # # # # # Loop Lab Repeat actions with a loop

# # # # # # for i in range(1, 10):
# # # # # #     print("Count:", i)


# # # # # # a = int(input("Enter a number: "))
# # # # # # b = int(input("Enter another number: "))
# # # # # # print("Adding them gives:", a + b)
# # # # # # print("But I think multiplying is cooler:", a * b)
# # # # # # print("Or maybe just subtracting for fun:", a - b)


# # # # # # Simple Calculator Project

# # # # # # def add(x, y):
# # # # # #     return x + y

# # # # # # def subtract(x, y):
# # # # # #     return x - y

# # # # # # def multiply(x, y):
# # # # # #     return x * y

# # # # # # def divide(x, y):
# # # # # #     try:
# # # # # #         return x / y
# # # # # #     except ZeroDivisionError:
# # # # # #         return "Error! Division by zero."

# # # # # # print("Welcome to the Python Calculator!")
# # # # # # print("Select operation:")
# # # # # # print("1. Add")
# # # # # # print("2. Subtract")
# # # # # # print("3. Multiply")
# # # # # # print("4. Divide")

# # # # # # while True:
# # # # # #     choice = input("Enter choice (1/2/3/4 or 'q' to quit): ")

# # # # # #     if choice == 'q':
# # # # # #         print("Goodbye! 👋")
# # # # # #         break

# # # # # #     if choice in ('1', '2', '3', '4'):
# # # # # #         try:
# # # # # #             num1 = float(input("Enter first number: "))
# # # # # #             num2 = float(input("Enter second number: "))
# # # # # #         except ValueError:
# # # # # #             print("Invalid input! Please enter numbers only.")
# # # # # #             continue

# # # # # #         if choice == '1':
# # # # # #             print("Result:", add(num1, num2))
# # # # # #         elif choice == '2':
# # # # # #             print("Result:", subtract(num1, num2))
# # # # # #         elif choice == '3':
# # # # # #             print("Result:", multiply(num1, num2))
# # # # # #         elif choice == '4':
# # # # # #             print("Result:", divide(num1, num2))
# # # # # #     else:
# # # # # #         print("Invalid choice! Please select 1, 2, 3, 4, or 'q'.")















# # # # # # import tkinter as tk

# # # # # # # Create main window
# # # # # # root = tk.Tk()
# # # # # # root.title("Python Calculator")

# # # # # # # Entry widget for display
# # # # # # entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
# # # # # # entry.grid(row=0, column=0, columnspan=4)

# # # # # # # Function to handle button clicks
# # # # # # def click_button(value):
# # # # # #     current = entry.get()
# # # # # #     entry.delete(0, tk.END)
# # # # # #     entry.insert(0, current + str(value))

# # # # # # def clear_button():
# # # # # #     entry.delete(0, tk.END)

# # # # # # def calculate():
# # # # # #     try:
# # # # # #         result = eval(entry.get())
# # # # # #         entry.delete(0, tk.END)
# # # # # #         entry.insert(0, str(result))
# # # # # #     except:
# # # # # #         entry.delete(0, tk.END)
# # # # # #         entry.insert(0, "Error")

# # # # # # # Button layout
# # # # # # buttons = [
# # # # # #     ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
# # # # # #     ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
# # # # # #     ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
# # # # # #     ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
# # # # # # ]

# # # # # # for (text, row, col) in buttons:
# # # # # #     if text == '=':
# # # # # #         tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
# # # # # #     else:
# # # # # #         tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click_button(t)).grid(row=row, column=col)

# # # # # # # Clear button
# # # # # # tk.Button(root, text="C", width=5, height=2, command=clear_button).grid(row=4, column=2)

# # # # # # # Run the app
# # # # # # root.mainloop()


# # # # # ##################################################################################################


# # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # fruits[1] = "orange"   # change banana to orange
# # # # # # fruits.append("grape") # add new item
# # # # # # print(fruits)  # ['apple', 'orange', 'cherry', 'grape']


# # # # # # coordinates = (10, 20)
# # # # # # print(coordinates[1])  # 10
# # # # # # # coordinates[0] = 15  ❌ Error: tuples cannot be changed


# # # # # # for i in range(1, 10,1):  # start=1, stop=6 (exclusive), step=1
# # # # # #     print(i)
# # # # # # # Output: 1 2 3 4 5




# # # # # # a = 23
# # # # # # b = 20
# # # # # # c = 10
# # # # # # d = "adkfdkflkfd"





# # # # # # x, y, z = "Orange", "Banana", "Cherry"
# # # # # # print(x)
# # # # # # print(y)
# # # # # # # print(z)


# # # # # # # x = "Python"
# # # # # # # y = "is"
# # # # # # # z = "awesome"
# # # # # # # print(x, y, z)

# # # # # # # x = "Python is awesome"
# # # # # # # print(x)

# # # # # # # mylist = ['apple', 'banana', 'cherry']
# # # # # # # print(mylist)


# # # # # # # thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# # # # # # # print(thislist)





# # # # # # x = 10
# # # # # # y = 3.5
# # # # # # name = "Python"
# # # # # # is_fun = True

# # # # # # if is_fun:
# # # # # #     print(f"{name} is fun!")
# # # # # #     print(f"x + y = {x + y}")





# # # # # # x = 15
# # # # # # y = 4

# # # # # # print(x + y)
# # # # # # print(x - y)
# # # # # # # print(x * y)
# # # # # # # print(x / y)
# # # # # # # print(x % y)
# # # # # # # # print(x ** y)
# # # # # # # # print(x // y)

# # # # # # # x = 5
# # # # # # # print(x)

# # # # # # # x += 3
# # # # # # # print(x)

# # # # # # # x -= 3
# # # # # # # print(x)

# # # # # # # x *= 3
# # # # # # # print(x)

# # # # # # # x /= 3
# # # # # # # print(x)

# # # # # # # x %= 3
# # # # # # # print(x)

# # # # # # # x **= 3
# # # # # # # print(x)






# # # # # # num = 6

# # # # # # # x = "WEEKEND!" if num > 5 else "Workday"

# # # # # # if num > 5:
# # # # # #     x = "Weekend!"
# # # # # # else:
# # # # # #     x = "Workdays!"
# # # # # # print(x)







# # # # # # Comparison Operators


# # # # # # x = 100
# # # # # # y = 30

# # # # # # print(x == y)
# # # # # # print(x != y)
# # # # # # print(x > y)
# # # # # # print(x < y)
# # # # # # print(x >= y)
# # # # # # print(x <= y)



# # # # # # Python Logical Operators


# # # # # # ram = 17
# # # # # # shyam = 19
# # # # # # man = 20

# # # # # # if not (ram > 18 and shyam > 18):
# # # # # #     print("eligible")
# # # # # # else:
# # # # # #     print("not eligible")

# # # # # # Python Identity Operators



# # # # # # x = [1,2,3]

# # # # # # y = x

# # # # # # z = [1,2,3]

# # # # # # # x[0] = 5

# # # # # # # print(x)
# # # # # # # print(y)


# # # # # # print(x == y)
# # # # # # print(x == z)
# # # # # # print(y == z)


# # # # # # print(x is y)
# # # # # # print(x is z)
# # # # # # print(y is z)


# # # # # # Python Membership Operators


# # # # # # a = [1,2,3,4,5]
# # # # # # b = (1,2,3,4,5)
# # # # # # c = {1,2,3,4,5}

# # # # # # print("adddfff" in a)
# # # # # # print(1 in b)
# # # # # # print(True in c)



# # # # # # age = 25
# # # # # # is_student = False
# # # # # # has_discount_code = True

# # # # # # if (age < 18 or age > 65) or not is_student or has_discount_code:
# # # # # #   print("Discount applies!")

# # # # # # score = 85
# # # # # # attendance = 90
# # # # # # submitted = True

# # # # # # if score >= 60:
# # # # # #   if attendance >= 80:
# # # # # #     if submitted:
# # # # # #       print("Pass with good standing")
# # # # # #     else:
# # # # # #       print("Pass but missing assignment")
# # # # # #   else:
# # # # # #     print("Pass but low attendance")
# # # # # # else:
# # # # # #   print("Fail")






# # # # # # Python Conditions and If statements
# # # # # # Python supports the usual logical conditions from mathematics:

# # # # # # Equals: a == b
# # # # # # Not Equals: a != b
# # # # # # Less than: a < b
# # # # # # Less than or equal to: a <= b
# # # # # # Greater than: a > b
# # # # # # Greater than or equal to: a >= b


# # # # # # day = 7
# # # # # # match day:
# # # # # #   case 1:
# # # # # #     print("Monday")
# # # # # #   case 2:
# # # # # #     print("Tuesday")
# # # # # #   case 3:
# # # # # #     print("Wednesday")
# # # # # #   case 4:
# # # # # #     print("Thursday")
# # # # # #   case 5:
# # # # # #     print("Friday")
# # # # # #   case 6:
# # # # # #     print("Saturday")
# # # # # #   case 7:
# # # # # #     print("Sunday")



# # # # # # day = 1
# # # # # # match day:
# # # # # #   case 6:
# # # # # #     print("Today is Saturday")
# # # # # #   case 7:
# # # # # #     print("Today is Sunday")
# # # # # #   case _:
# # # # # #     print("Looking forward to the Weekend")


# # # # # # day = 4
# # # # # # match day:
# # # # # #   case 1 | 2 | 3 | 4 | 5:
# # # # # #     print("Today is a weekday")
# # # # # #   case 6 | 7:
# # # # # #     print("I love weekends!")


# # # # # # month = 6
# # # # # # day = 1
# # # # # # match day:
# # # # # #   case 1 | 2 | 3 | 4 | 5 if month == 4:
# # # # # #     print("A weekday in April")
# # # # # #   case 1 | 2 | 3 | 4 | 5 if month == 5:
# # # # # #     print("A weekday in May")
# # # # # #   case _:
# # # # # #     print("No match")



# # # # # # Python Loops
# # # # # # Python has two primitive loop commands:

# # # # # # while loops
# # # # # # for loops

# # # # # # The while Loop
# # # # # # With the while loop we can execute a set of statements as long as a condition is true.



# # # # # # for i in range(10,20,5):
# # # # # #     print(i)

# # # # # # x = int(input("enter a integer:"))

# # # # # # while x!=0:
# # # # # #     x = x//2
# # # # # #     print(x)

# # # # # # print("x has reached 0 or below 0")


# # # # # # The continue Statement
# # # # # # With the continue statement we can stop the current iteration, and continue with the next:



# # # # # # The break Statement
# # # # # # With the break statement we can stop the loop even if the while condition is true:

# # # # # # for i in range(1,11,1):

# # # # # #     # if i == 5 or i ==9:
# # # # # #     #     continue
# # # # # #     # print(i)

# # # # #     # print(i, end=" - ")
# # # # #     # print(1, end=" ")
# # # # #     # print(2, end=" ")
# # # # #     # if i == 5:
# # # # #     #     print()
# # # # #     #     continue
# # # # #     # print(3, end=" ")
# # # # #     # print(4, end=" ")
# # # # #     # print(5)





# # # # # # i = 1
# # # # # # while i != 11:
# # # # # #     print(i, end=" - ")
# # # # # #     print(1, end=" ")
# # # # # #     print(2, end=" ")
# # # # # #     if i == 5:
# # # # # #         print()
# # # # # #         continue
# # # # # #     print(3, end=" ")
# # # # # #     print(4, end=" ")
# # # # # #     print(5)



# # # # # # MYNAME1 = "ABC"
# # # # # # print(MYNAME1)


# # # # # # a = [1,2,3,4,5,6]

# # # # # # a.insert(20, 50)

# # # # # # print(a)


# # # # # # a = int(input("Enter a value for A: "))
# # # # # # b = int(input("Enter a value for B: "))

# # # # # # print(a+b)


# # # # # # Text
# # # # # # text = "Python"

# # # # # # # Numbers
# # # # # # num_int = 10
# # # # # # num_float = 3.14
# # # # # # num_complex = 2 + 3j

# # # # # # # Sequence
# # # # # # my_list = [1, 2, 3]
# # # # # # my_tuple = (4, 5, 6)
# # # # # # my_range = range(3)

# # # # # # # Mapping
# # # # # # my_dict = {"name": "Alice", "age": 25}

# # # # # # # Set
# # # # # # my_set = {1, 2, 3}
# # # # # # my_frozenset = frozenset([4, 5, 6])

# # # # # # # Boolean
# # # # # # is_active = True

# # # # # # # Binary
# # # # # # my_bytes = b"hello"
# # # # # # my_bytearray = bytearray([65, 66, 67])
# # # # # # my_memoryview = memoryview(b"world")

# # # # # # # None
# # # # # # nothing = None

# # # # # # print(type(text), type(num_int), type(my_list), type(my_dict), type(my_set), type(is_active), type(my_bytes), type(nothing))



# # # # # # numbers = [1, 2, 2, 3, 4, 4, 5]
# # # # # # unique_numbers = set(numbers)
# # # # # # print(unique_numbers)      
# # # # # # print(len(unique_numbers))


# # # # # # x = input("Enter something: ")
# # # # # # print(x)



# # # # # # text = "Hello hello HELLO"
# # # # # # print(text.count("hello")) 
# # # # # # print(text.lower().count("hello"))
      

# # # # # # b = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

# # # # # # b = set(b)
# # # # # # b = list(b)

# # # # # # print(b)


# # # # # # # a = "Greeting the Data type"

# # # # # # # print(a[-2:])


# # # # # # # a = "Greeting the Data type"


# # # # # # # words = a.split()  


# # # # # # # print(" ".join(words[-2:]))







# # # # # # # a = {1,2,3}
# # # # # # # a = set({1,2,3})

# # # # # # # fs = frozenset(a)



# # # # # # # data = b"Hello"

# # # # # # # data_from_list = ([72,101,108,111])

# # # # # # # print(data[3])


# # # # # # # a = int(input("enter a number between 1-10"))

# # # # # # # if a >= 1 and a <= 10:
# # # # # # #     print("True")
# # # # # # # else:
# # # # # # #     print("False")


# # # # # # # match a:
# # # # # # #     case 1 | 2 | 3 | 4| 5 | 6 | 7 | 8 | 9 | 10
# # # # # # #        print("True")
# # # # # # #     case _: 
# # # # # # #         print("False") 





# # # # # # day = "Sunday"

# # # # # # match day:
# # # # # #     case "Monday":
# # # # # #         print("Start of the work week!")
# # # # # #     case "Tuesday":
# # # # # #         print("Second day of the week.")
# # # # # #     case "Wednesday":
# # # # # #         print("Midweek already.")
# # # # # #     case "Thursday":
# # # # # #         print("Almost Friday!")
# # # # # #     case "Friday":
# # # # # #         print("Weekend is near.")
# # # # # #     case "Saturday":
# # # # # #         print("Enjoy your weekend!")
# # # # # #     case "Sunday":
# # # # # #         print("Relax, it's Sunday.")
# # # # # #     case _:
# # # # # #         print("Not a valid day.")



# # # # # a = int(input("Enter a number between 1-7: "))

# # # # # if a == 1:
# # # # #     print("Sunday")
# # # # # elif a == 2:
# # # # #     print("Monday")
# # # # # elif a == 3:
# # # # #     print("Tuesday")
# # # # # elif a == 4:
# # # # #     print("Wednesday")
# # # # # elif a == 5:
# # # # #     print("Thursday")
# # # # # elif a == 6:
# # # # #     print("Friday")
# # # # # elif a == 7:
# # # # #     print("Saturday")
# # # # # else:
# # # # #     print("Invalid number! Please enter between 1-7.")







# # # # # x = int(input("Enter a integer:"))

# # # # # while x!=0:
# # # # #     x = x//2
# # # # #     print(x)

# # # # # print("X has reached 0 ")


# # # # # a = 0

# # # # # while True:
# # # # #     print(a)

# # # # #     a += 1



# # # # # count = 1
# # # # # while count <= 5:
# # # # #     print(count)
# # # # #     count += 1   # increase count by 1



# # # # # x = 0
# # # # # while x < 10:
# # # # #     x += 1
# # # # #     if x == 5:
# # # # #         continue   # skip printing 5
# # # # #     if x == 9:
# # # # #         break      # stop loop at 8
# # # # #     print(x)


# # # # # a = "Name"

# # # # # # print(a*3)

# # # # # print("Hello")
# # # # # print("Hello", end=" A! ")
# # # # # print("Hello", end=" B! ")
# # # # # print("Hello", end=" C! ")

      

# # # # # a = "*"

# # # # # for i in range(6, 0, -1):
# # # # #     print(a*i)




# # # # # for i in range(1,7):
# # # # #     for j in range(6-i):
# # # # #         print(" "*j, end="")



# # # # #     for k in range(i):
# # # # #         print("*", end=" ")
# # # # # print()
# # # # # # 


# # # # for i in range(1, 7):
  
# # # #     for j in range(6 - i):
# # # #         print(" ", end="")

# # # #     for k in range(i):
# # # #         print("*", end=" ")
  
# # # #     print()








# # # # # a = 6   # number of rows

# # # # # for i in range(a, 0, -1):   # start from 6 down to 1
# # # # #     # print spaces
# # # # #     for j in range(a - i):
# # # # #         print(" ", end="")

# # # # #     # print stars
# # # # #     for k in range(i):
# # # # #         print("*", end=" ")

# # # # #     # move to next line
# # # # #     print()






# # # # def fun():
# # # #     print("Hello World")
# # # #     for i in range(1,10,):
# # # #         print(i**i)


# # # # fun()



# # # # def greet(name):
# # # #     print("Hello", name)

# # # # greet("Uttam")




# # # # def faranhit_to_celcius(fahrenheit):
# # # #     celsius = (fahrenheit - 32) * 5 / 9
# # # #     return celsius

# # # # faranhit = 12
# # # # celsius = faranhit_to_celcius(fahrenheite)
# # # # msg = f"Todays temp is {celsius}"

# # # # print(msg)




# # # # def my_function(name):
# # # #     print("Hello", name)

# # # # my_function("Email")
# # # # my_function("abc")
# # # # my_function()
# # # # my_function("xyz")


# # # # def greet():
# # # #     print("Hello, welcome to Python!")
# # # # greet()


# # # # def my_function():
# # # #   return ["apple", "banana", "cherry"]

# # # # fruits = my_function()
# # # # print(fruits[0])
# # # # print(fruits[1])
# # # # print(fruits[2])


# # # # def my_function():
# # # #   return (10, 20, 50)

# # # # x, y, z = my_function()
# # # # print("x:", x)
# # # # print("y:", y)
# # # # print("z:", z)



# # # #arga and kwargs



# # # # def my_function(*kids):
# # # #  print("the yougest child is ", kids)

# # # # my_function("Email", "Tobias", "linus")



# # # # ?wargs


# # # # def my_function(*kids):
# # # #  print("the third child is ", kids['third_child'])

# # # # my_function(first_child="Email", second_child="Tobias", third_child="linus")



# # # # def my_function(a, b, c):
# # # #   return a + b + c

# # # # numbers = [1, 2, 3]
# # # # result = my_function(*numbers) # Same as: my_function(1, 2, 3)
# # # # print(result)



# # # # students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# # # # sorted_students = sorted(students, key=lambda x: x[1])
# # # # print(sorted_students)


# # # # def factorial(n):
# # # #   # Base case
# # # #   if n == 0 or n == 1:
# # # #     return 1
# # # #   # Recursive case
# # # #   else:
# # # #     return n * factorial(n - 1)

# # # # print(factorial(5))



# # # # def my_generator():
# # # #   yield 1
# # # #   yield 2
# # # #   yield 3

# # # # for value in my_generator():
# # # #   print(value)



# # # # import datetime 

# # # # x = datetime.datetime.now()

# # # # print(x)



# # # # from datetime import datetime
# # # # x = datetime.now()

# # # # print(x.strftime("%d-%b-%y %I:%M%S %p"))






# # # # import mysql.connector

# # # # mydb = mysql.connector.connect(
# # # #   host="localhost",
# # # #   user="root",
# # # #   password="root",
# # # # #   database = "pyhon_batch"

# # # # )



# # # # print(mydb)

# # # # # mycursor = mydb.cursor()

# # # # # # # mycursor.execute("CREATE DATABASE pyhon_batch")
# # # # # # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# # # # # # mycursor.execute("SHOW TABLES")

# # # # # # for x in mycursor:
# # # # # #   print(x)


# # # # # # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# # # # # # val = [
# # # # # #   ('Peter', 'Lowstreet 4'),
# # # # # #   ('Amy', 'Apple st 652'),
# # # # # #   ('Hannah', 'Mountain 21'),
# # # # # #   ('Michael', 'Valley 345'),
# # # # # #   ('Sandy', 'Ocean blvd 2'),
# # # # # #   ('Betty', 'Green Grass 1'),
# # # # # #   ('Richard', 'Sky st 331'),
# # # # # #   ('Susan', 'One way 98'),
# # # # # #   ('Vicky', 'Yellow Garden 2'),
# # # # # #   ('Ben', 'Park Lane 38'),
# # # # # #   ('William', 'Central st 954'),
# # # # # #   ('Chuck', 'Main Road 989'),
# # # # # #   ('Viola', 'Sideway 1633')
# # # # # # ]

# # # # # # mycursor.executemany(sql, val)

# # # # # # mydb.commit()

# # # # # # print(mycursor.rowcount, "was inserted.")


# # # # # # mycursor.execute("SELECT * FROM customers")

# # # # # # myresult = mycursor.fetchall()

# # # # # # for x in myresult:
# # # # # #   print(x)

# # # # # mycursor.execute("SELECT name, address FROM customers")

# # # # # myresult = mycursor.fetchall()

# # # # # for x in myresult:
# # # # #   print(x)














# # # import mysql.connector

# # # mydb = mysql.connector.connect(
# # #   host="localhost",
# # #   user="root",
# # #   password="root",
# # #   database = "NewDataBase"

# # # )

# # # # print("connected")
# # # # cursor()


# # # Mycursor = mydb.cursor()


# # # # Mycursor.execute("show tables")

# # # # Mycursor.execute("INSERT INTO Employee (id, name, city) VALUES (1, 'A', 'Delhi'),(2, 'B', 'Mumbai'),(3, 'C', 'Pune')")
# # # # # Mycursor.execute("INSERT INTO Employee (id, name, city) VALUES (2, 'B', 'Mumbai')")
# # # # # Mycursor.execute("INSERT INTO Employee (id, name, city) VALUES (3, 'C', 'Pune')")
# # # # mydb.commit()   


# # # # Mycursor.execute("show tables")

# # # # for i in Mycursor:
# # # #     print(i[0])


# # # # Mycursor.execute("drop table Employee")



# # # # Mycursor.execute("create table Python (id int, name varchar(255), city varchar(255))")


# # # # Mycursor.execute("INSERT INTO Python (id, name, city) VALUES (1, 'A', 'Delhi'),(2, 'B', 'Mumbai'),(3, 'C', 'Pune')")
# # # # mydb.commit()



# # # Mycursor.execute("select * from Python")

# # # for i in Mycursor:
# # #     print(i)

# # # # Mycursor.execute("update Python set city = 'Chennai' where id = 1")
# # # # mydb.commit()

# # # # for i in Mycursor:
# # # #     print(i)



# # # # Mycursor.execute("Delete from Python where id = 1")
# # # # mydb.commit()

# # # # for i in Mycursor:
# # # #     print(i)



# # # oops

# # # procedrual function based

# # # ex - lang case

# # # oops classes and object

# # # ex - lang python, java, c++, c#

# # # from copyreg import constructor


# # # constructor 

# # # Note: The __init__() method is called automatically every time the class is being used to create a new object.


# # # Why Use __init__()?
# # # Without the __init__() method, you would need to set properties manually for each object:





# # class info:
# #     def setValues(self, name, age):
# #         self.name = name
# #         self.age = age
# #         # self.weight = weight



# #     def showName(self):
# #             print( self.name)


# #     def showAge(self):
# #             print(self.age)





# # obj = info()
# # obj.setValues("Anurudh", 25)
# # obj.showName()


# # obj1 = info()
# # obj1.setValues("Uttam", 30)
# # obj1.showName()


# # # print(obj.name, obj.age, obj.weight)
# # # print(obj.weight)



# # # obj1 = info()
# # # obj1.setValues("Uttam", 30, 80)
# # # print(obj1.name, obj1.age, obj1.weight)
# # # print(obj1.weight)





# # class Num:
# #     def _init__(self, num):
# #         self.num = num

# #     def check_even_odd(self):
# #         if self.num % 2 == 0:
# #             return "Even"
# #         else:
# #             return "Odd"

        



# # class Num:
# #     def __init__(self, num):
# #         self.num = num

# #     def check():
# #         pass

# #     def sq():
# #         pass





# class Num:
#     def __init__(self, num):
#         self.num = num

#     def check(self):
#         if self.num % 2 == 0:
#             return "Even"
#         else:
#             return "Odd"

#     def sq(self):
#         return self.num ** 2

# # Example usage
# n = Num(1)
# print(n.check())  # Odd
# print(n.sq())     # 25



# from py_compile import main


# 4 main pillars of oops
# 1. Encapsulation      
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
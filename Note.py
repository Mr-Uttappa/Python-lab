# # (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\Uttam\Downloads\Python-Batch\.Hello\Scripts\Activate.ps1)




# # name = "Uttappa"

# # Age = 30

# # Weight = 76.70


# # print(type(name))
# # print(type(Age))
# # print(type(Weight))



# a = "Name"

# print("a")




import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",      # your MySQL server
    user="root",           # your username
    password="root",   # your password
    database="MYDB"       # database name
)

cursor = conn.cursor()


# print(conn)



cursor.execute("""
CREATE TABLE MYDB (
    id INT,
    name VARCHAR(50),
    city VARCHAR(50)
)
""")



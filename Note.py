# # # (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\Uttam\Downloads\Python-Batch\.Hello\Scripts\Activate.ps1)




# # # name = "Uttappa"

# # # Age = 30

# # # Weight = 76.70


# # # print(type(name))
# # # print(type(Age))
# # # print(type(Weight))



# # a = "Name"

# # print("a")




# import mysql.connector

# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",      # your MySQL server
#     user="root",           # your username
#     password="root",   # your password
#     database="MYDB"       # database name
# )

# cursor = conn.cursor()


# # print(conn)



# cursor.execute("""
# CREATE TABLE MYDB (
#     id INT,
#     name VARCHAR(50),
#     city VARCHAR(50)
# )
# """)





import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="your_password",  # your MySQL password
    database="DBB"      # the database you created
)

cursor = conn.cursor()

# --- CREATE (Insert) ---
cursor.execute("INSERT INTO students (id, name, city) VALUES (1, 'Anurudh', 'Delhi')")
cursor.execute("INSERT INTO students (id, name, city) VALUES (2, 'Arun', 'Mumbai')")
cursor.execute("INSERT INTO students (id, name, city) VALUES (3, 'Abhi', 'Pune')")
conn.commit()   # save changes

# --- READ (Select) ---
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Students:")
for row in rows:
    print(row)

# --- UPDATE ---
cursor.execute("UPDATE students SET name='Anuruddh' WHERE id=1")
conn.commit()

# --- DELETE ---
cursor.execute("DELETE FROM students WHERE id=2")
conn.commit()

# --- TRUNCATE (Clear all data) ---
cursor.execute("TRUNCATE TABLE students")
conn.commit()

# Close connection
cursor.close()
conn.close()

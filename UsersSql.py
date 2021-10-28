import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testuser",
  password="test1234"
  database="UserDB"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), email VARCHAR(255)), phone CHAR(10)")

sql = "INSERT INTO customers (fname, lname, email, phone) VALUES (%s, %s, %s, %s)"
val = [
  ('Elmer', 'Sanchez', 'ejs32@njit.edu', '9735555001'),
  ('Jared', 'Myers', 'jm297@njit.edu', '9735555002'),
  ('Wyatt', 'Eynon', 'wme4@njit.edu', '9735555003'),
  ('Rebecca', 'Sorkin', 'rls34@njit.edu', '9735555004')
]
mycursor.executemany(sql, val)

mydb.commit()

import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin123",
  database="DemoBD"
)


mycursor = mydb.cursor()

query = "SELECT * from Student;"
q2 = "SELECT  FirstName = 'Priya'  from Student;"
q1 = "INSERT INTO Student(StudentId,FirstName,LastName,Address,City)VALUES ('1002','Priya','sing','marathalli','Bangalore');"

mycursor.execute(q2)
fetch = mycursor.fetchall()
mydb.commit()

for i  in fetch:
    print(i)

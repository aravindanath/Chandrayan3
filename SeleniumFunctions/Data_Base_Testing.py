import mysql.connector



"""
Study material for python mysql

Need to add 'mysql-connector' pkg using PIP

https://pynative.com/python-mysql-database-connection/


"""




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin123",
  database="DemoBD"
)

mycursor = mydb.cursor()

# mycursor.execute("show databases")
query = "SELECT * from Employee;"
q ="INSERT INTO Employee  VALUES (1001, 'Kshama', 'Sheetal', 'Delhi','Bangalore','java');"
mycursor.execute(query)

fetch = mycursor.fetchall()

# for i in mycursor:
#     print(i)

mydb.commit()
#
for i in fetch:
    print(i)


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="poonamsharma",
  database="mydatabase"
)

mycursor = mydb.cursor()


sqla = "DROP TABLE pass_detail"
mycursor.execute(sqla)

sqlb = "DROP TABLE transport"
mycursor.execute(sqlb)

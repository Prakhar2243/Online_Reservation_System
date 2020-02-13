import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="poonamsharma",
  database="mydatabase"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE pass_detail (pnr INT PRIMARY KEY NOT NULL, fname VARCHAR(25) NOT NULL, lname VARCHAR(25) NOT NULL, gender VARCHAR(25) NOT NULL, age INT NOT NULL, phone_no INT NOT NULL, bpoint VARCHAR(25) NOT NULL, dpoint VARCHAR(25) NOT NULL, slot VARCHAR(25) NOT NULL)")
mydb.commit()

mycursor.execute('CREATE TABLE transport (initial_city VARCHAR(25) NOT NULL, final_city VARCHAR(25) NOT NULL, slot VARCHAR(25) NOT NULL, avail int NOT NULL, bus_no int PRIMARY KEY NOT NULL, driver_name VARCHAR(25) NOT NULL)')
mydb.commit()


mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('mumbai','chennai', 'morning-5:00', 40, 1121, 'praveen')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('mumbai','delhi', 'morning-6:00', 40, 1123, 'ashwin')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('mumbai','banglore', 'morning-7:00', 40, 1131, 'arun')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('delhi','chennai', 'morning-8:00', 40, 1125, 'aditya')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('delhi','banglore', 'morning-9:00', 40, 1129, 'aman')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('chennai','banglore', 'morning-10:00', 40, 1127, 'vibhuti')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('banglore','mumbai', 'evening-5:00', 40, 1132, 'arun')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('banglore','delhi', 'evening-6:00', 40, 1130, 'aman')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('banglore','chennai', 'evening-7:00', 40, 1128, 'vibhuti')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('chennai','mumbai', 'evening-8:00', 40, 1122, 'praveen')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('chennai','delhi', 'evening-9:00', 40, 1126, 'aditya')")
mycursor.execute("INSERT INTO transport (initial_city, final_city, slot, avail, bus_no, driver_name) VALUE ('delhi','mumbai', 'evening-10:00', 40, 1124, 'ashwin')")
mydb.commit()

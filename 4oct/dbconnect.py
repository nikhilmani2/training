import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="hospital")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM patient")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except mysql.connector.Error as e:
    print("Error connecting to database:", e)

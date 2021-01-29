import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01")
mycursor = mydb.cursor()
#mycursor.execute("create database studentdb")

mycursor.execute("show databases")
for i in mycursor:
    print(i)
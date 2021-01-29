import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01")
mycursor = mydb.cursor()
mycursor.execute("create database studentdb")
# you should make the aboue statement(  mycursor.execute("create database studentdb")  ) as comments after you run it once ( WHY? Ans: we cannot create the same database multiple times)
mycursor.execute("show databases")
for i in mycursor:
    print(i)

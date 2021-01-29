import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01",database = "studentdb")
mycursor=mydb.cursor()

#mycursor.execute("Create table student(name varchar (200),rno int(20) primary key)")
mycursor.execute("show tables")
for tb in mycursor:
    print(tb)
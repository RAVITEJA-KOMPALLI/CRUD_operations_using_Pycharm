import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01",database = "studentdb")
mycursor=mydb.cursor()

mycursor.execute("select * from student")
for i in mycursor:
    print(i)
import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01",database = "studentdb")
mycursor=mydb.cursor()

form="Insert into student(rno,name) values(%s,%s)"
students=[(202,"Ravi Teja"),(0,"Bablu")]
mycursor.executemany(form,students)
mydb.commit()
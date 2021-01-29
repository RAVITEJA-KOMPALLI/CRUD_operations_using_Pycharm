import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01",database = "studentdb")
mycursor=mydb.cursor()
# note we have given rno as a primary key so we should not repeat the values of rno
form="insert into student(rno,name) values(%s,%s)"
students=[(202,"Ravi Teja"),(0,"Bablu")]
mycursor.executemany(form,students)

'''
we can also write as follows:

mycursor.execute("insert into student(rno,name) values(202,"Ravi Teja"),(0,"Bablu")")
'''

mydb.commit()

# note commit is neccessary as it saves our changes/reflect our changes in our mysql database
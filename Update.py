import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01",database = "studentdb")
mycursor=mydb.cursor()

sql ="Update student SET rno=1 WHERE name='Bablu'"
mycursor.execute(sql)
mydb.commit()
# note commit is neccessary as it saves our changes/reflect our changes in our mysql database
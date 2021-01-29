import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01")
if mydb:
    print("Your database is connected successfully")
else:
    print("You have an error in database connection")
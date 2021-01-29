# Basic requirements -> python environment like pycharm & mysql database installed in your System
# install the mysql-connector in your System / if in the environment like Pycharm etc

'''
Steps to install mysql-connector in pycharm:
step 1: click on file
step 2: click on settings
step 3: click on 'project:pythonprj'  (in my case it is pythonprj the name will vary according to the project filename you have given)
step 4: click on ' python interpretor '
step 5: click on ' click on ' + ' icon  '
step 6: search mysql-connector in the search bar and then click on install
step 7: after installation click on OK

and now you have installed mysql-connector in your environment successfully
'''

import mysql.connector as m

# the password given below may vary from user to user -> enter your mySql password

mydb = m.connect(host = "localhost",user = "root", password = "Raviteja@01")
if mydb:
    print("Your database is connected successfully")
else:
    print("You have an error in database connection")

'''
if you are having an authentication error  while connecting database perform the below operations:

step 1: open MySQL installer 
step 2: click of reconfiguire of the 'mysql server' row 
step 3: click on next till you reach the authentication method 
step 4: now select 'use legacy authentication .... ' 
step 5: click on next 
step 6: type your mysql password 
step 7: click on check (you will be getting green tick if not ur entered password is wrong)
step 8: click on next 
step 9: again click on next
step 10: click on execute 
step 11: click on finish  

Now Try reconnecting/rerunning 

'''
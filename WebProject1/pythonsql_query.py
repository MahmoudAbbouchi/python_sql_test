#This is a python test code to attept to read from an sql database
import sqlite3
sqlconnection = sqlite3.connect("company.db")

cursor = sqlconnection.cursor()

sql_command = "SELECT * FROM employee;"
cursor.execute(sql_command)
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)

cursor.execute("SELECT * FROM employee") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)


#   exec(open("C:\\test.py").read()) TO RUN FOR SQL TUTORIAL WITH MULTIPLE FILES

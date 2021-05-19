#This is a python test code to attept to host/initialize an sql database
#Sample code for the IEEE CSRC Software Fundementals SQL and Database
#Change at will
#Author: Mahmoud Abbouchi
import sqlite3
sqlconnection = sqlite3.connect("company.db") #Create and connect to company.db

cursor = sqlconnection.cursor() #Initialize an SQL Cursor

sql_command = "DROP TABLE IF EXISTS employee;"
cursor.execute(sql_command)
sql_command = "DROP TABLE IF EXISTS company;"
cursor.execute(sql_command)

sql_command = """
CREATE TABLE employee (
company_id INTEGER,
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)

sql_command = """
CREATE TABLE company (
company_id INTEGER PRIMARY KEY, 
name VARCHAR(20), 
stock_id VARCHAR(30), 
creation DATE);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee (company_id, staff_number, fname, lname, gender, birth_date)
    VALUES (1, 1, "William", "Shakespeare", "m", "1961-10-25");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee (company_id, staff_number, fname, lname, gender, birth_date)
    VALUES (1, 2, "Johnny", "David", "m", "1975-03-15");"""
cursor.execute(sql_command)


sql_command = """INSERT INTO employee (company_id, staff_number, fname, lname, gender, birth_date)
    VALUES (2, 3, "Frank", "Schiller", "m", "1955-08-17");"""
cursor.execute(sql_command)


sql_command = """INSERT INTO company (company_id, name, stock_id, creation)
    VALUES (1, "Ryerson", "RYE", "1852-03-23");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO company (company_id, name, stock_id, creation)
    VALUES (2, "The Pierce Monument", "TPM", "2002-01-13");"""
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
sqlconnection.commit()


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

cursor.execute("SELECT * FROM company")
print("\ncompanies:")
cmpy = cursor.fetchall()
print(cmpy)


sql_command = """
SELECT * FROM employee
WHERE "company_id" IN (SELECT company_id
FROM company WHERE stock_id == "RYE");
"""
cursor.execute(sql_command)
print("\nsomething:\n")
smth = cursor.fetchall()
print(smth)


import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
   try:
     conn = sqlite3.connect('mydatabase.db')
     return conn
   except Error:
     print(Error)
 
def sql_table(conn):
   cursorObj = conn.cursor()
# Create the table
   cursorObj.execute("CREATE TABLE salesman4(EMPLOYE_id n(9), name char(30), city char(35));")
# Insert records
   cursorObj.executescript("""
   INSERT INTO salesman4 VALUES('BAJIBABA', 'ODOO','ATM');
   INSERT INTO salesman4 VALUES('KISHORE', 'ODOO I','ATM');
   INSERT INTO salesman4 VALUES('NIRANJAN', 'BUSSINESS','ATM');
   INSERT INTO salesman4 VALUES('MANOHAR', 'WEB DESIGN','ATM');
   INSERT INTO salesman4 VALUES('KIRAN', 'DEVELOPMENT','ATM');
   """)
   conn.commit()
   cursorObj.execute("SELECT * FROM salesman4")
   rows = cursorObj.fetchall()
   print("EMPLOYEE DETAILS:")
   for row in rows:
       print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")

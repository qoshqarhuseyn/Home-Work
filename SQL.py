import sqlite3

db = sqlite3.connect('atm.db')

sql = db.cursor()

sql.execute (""" CREATE TABLE IF NOT EXISTS atm(

    pin INT,
    balance INT
        
    
    ) """)

sql.execute("INSERT INTO atm (pin, balance) VALUES (8989, 800)")
db.commit()

choice = input("Choice: (1) Balance (2) Cash (3) Deposits (4) Change Pin (5) Exit ")

check = int (input("Enter your pin"))

while True:

  if check == sql.execute("Select * from pin"):
    choice = input("(1) Balance (2) Cash (3) Deposits (4) Change Pin (5) Exit")

    
    if choice == "1":
    
     sql.execute("Select * FROM atm 'balance'")
     print(sql)
    sql.execute("Select * FROM atm 'balance'")
    



















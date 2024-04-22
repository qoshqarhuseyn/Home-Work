
import sqlite3
import random

sq = sqlite3.connect('casino.db')
sql = sq.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS casino (
                    
    login VARCHAR (50),
    password VARCHAR (50),
    cash INT        
            
            )""")


print('Welcome to the casino!')

while True:

    choice = input('Choice: (1) Register (2) Play (3) Remove user from database (4) Check balance (5) Exit: ')

    if choice == '1':
        login = input('Enter your login (only letters and numbers): ')
        password = input('Enter your password  (only letters and numbers): ')
        cash = int(input('Enter your initial cash amount: '))
        sql.execute('INSERT INTO casino (login, password, cash) VALUES (?, ?, ?)', (login, password, cash))
        sq.commit()
        print('Registration successful!')

    elif choice == '2':
        balance = sql.execute('SELECT cash FROM casino WHERE login=?', (login,)).fetchone()[0]
        if balance < 5:
            print('Insufficient funds')
        else:
            result = random.choice(['win', 'lose'])
            if result == 'win':
                print('You have won 10 azn')
                balance += 10
            else:
                print('You lost 5 azn')
                balance -= 5
            sql.execute('UPDATE casino SET cash=? WHERE login=?', (balance, login))
            sq.commit()

    elif choice == '3':
        while True:
            check1 = input('Are you sure? y/n: ')
            if check1 == 'y':
                sql.execute('DELETE FROM casino WHERE login=?', (login,))
                sq.commit()
                print('User removed from database')
                login = None 
                break  
            elif check1 == 'n':
                print('Canceling actions. Return to selection menu')
                break 
            else:
                print('Invalid choice. Please enter y/n.')
                continue  

    elif choice == '4':
        balance = sql.execute('SELECT cash FROM casino WHERE login=?', (login,)).fetchone()
        if balance:
            print(f'Your current balance is {balance[0]} azn')
        else:
            print('User not found.')

    elif choice == '5':
        print('Exiting the game...')
        break
    
    else:
        print('Invalid choice. Try again.')
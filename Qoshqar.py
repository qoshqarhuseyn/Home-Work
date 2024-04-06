

# Task - 1




# def factorial(n):

#     if n == 0:
     
#         return 1
#     else:
   
#         return n * factorial(n - 1)


# n = int(input("Enter the factorial: "))


# print(factorial(n))




# Task - 2



# def reverse():
#     word = input('Enter a word: ')
#     reversed_word = word[::-1]
#     return reversed_word
# right = reverse()
# print("Word from right to left:", right)







# Task - 3







# def process_sentences(sentence1, sentence2):
#     def print_first_sentence(sentence):
#         sentences = sentence.split('.')
#         if len(sentences) >= 1:
#             first_sentence = sentences[0].strip().upper()
#             print(first_sentence + '.')
#         else:
#             print(sentence)

#     print("first sentence:")
#     print_first_sentence(sentence1)
#     print("\nThe first sentence of the second sentence:")
#     print_first_sentence(sentence2)


# cümle1 = input("first sentence: ")
# cümle2 = input("second sentence: ")
# process_sentences(cümle1, cümle2)


    


#  Task - 4



# sen1= input("soz yaz:")
# sen2= input("soz yaz":)







# Task - 5


# def calculate_exponent(num1, num2):
#     result1 = num1 ** num2
#     return result1

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# result1 = calculate_exponent(num1, num2)

# print(f"{num1} raised to the power of {num2} is: {result1}")




# Task - 6




# def reverse():
#     word = input('Enter a word: ')
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return 'palindrome'
#     else:
#         return reversed_word
# right = reverse()
# print("Word from right to left:", right)






















# Task - 7




# print("Enter a Number: ")
# num = int(input())

# squareroot = num (map(lambda x: x ** 5, ))

# print("\nSquare Root =", squareroot)




# Task - 8



# ss = [5, 7, 9, 16, 20]

# square_nums = list(map(lambda x: x ** 2, ss))
# print(square_nums)












# def access_to_scholl(self):
#     if self.age >17:
#         return "olar"
#     else:
#         return "olmaz"
#     register = register(name="Orxan")









# Task - 1



# name_ = input("Enter the employee name")
# age_ =  int(input ("Enter the employrr name"))
# id_ = input("Enter employee id")
# salary_ = input("Enter the salary")
# maas_ = int(input("Enter the maas"))
# department_ = (input("Enter the department employee"))


# class Employee:
      
#     def __init__(self, emp_id, emp_name, emp_maas, emp_department, emp_salary, emp_age):
        
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         self.emp_name = emp_name
#         self.emp_maas = emp_maas
#         self.emp_department = emp_department
#         self.emp_age = emp_age

#     def assign_department(self, new_department):
#         self.emp_department = new_department
        
#         print (f"{self.emp_name} not assingned to department: {self.emp_department}")

#     def calculate_emp_salary(self, emp_hours_worker):
        
#         if emp_hours_worker >50:
#             return self.emp_salary
        




# Task - 2

# class Bankaccount:
#     def __init__(self):
#         self.balance = 0

#         print("Hello, Welcome to the deposits and Withdraval machine")


        





# Task - 1



# class Employee:
#     def _init_(self, emp_name, emp_id, emp_salary, emp_department):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department

#     def calculate_emp_salary(self, hours_worked):
#         if hours_worked > 50:
#             overtime = hours_worked - 50
#             overtime_amount = overtime * (self.emp_salary / 50)
#             total_salary = self.emp_salary + overtime_amount
#             return total_salary
#         else:
#             return self.emp_salary

#     def emp_assign_department(self, new_department):
#         self.emp_department = new_department

#     def print_employee_details(self):
#         print("Employee Name:", self.emp_name)
#         print("Employee ID:", self.emp_id)
#         print("Employee Salary:", self.emp_salary)
#         print("Employee Department:", self.emp_department)


# # Sample Employee Data
# employees_data = [
#     ("ADAMS", "E7876", 50000, "ACCOUNTING"),
#     ("JONES", "E7499", 45000, "RESEARCH"),
#     ("MARTIN", "E7900", 50000, "SALES"),
#     ("SMITH", "E7698", 55000, "OPERATIONS")
# ]

# # Creating employee objects and demonstrating methods
# for emp_data in employees_data:
#     emp = Employee(*emp_data)
#     print("\nInitial Details:")
#     emp.print_employee_details()
#     print("Updated Salary after overtime:", emp.calculate_emp_salary(55))
#     emp.emp_assign_department("HR")
#     print("Updated Department:", emp.emp_department)








# # Home
# class calisan:

#  def __init__(self, name, surname, age):

#     print("__init__funksiyasi isleyir")
#     self.name = name
#     self.surname = surname
#     self.age = age



# def show_info(self):
#   ptint(f"Ad:{self.name} Soyad: 

# calisan1 = calisan("Ali", "Veli", 20)
# print(calisan1.name, calisan1.surname,calisan1.age)



# calisan2 = calisan("Ahmet", "Mehmet", 25)

# print(calisan2.name,calisan2.surname,calisan2.age)








# Task - 1



# import datetime 
# import calendar 

# weekdays = ["Monday", "Tuesday", "Wednesday", 
# 		"Thursday", "Friday", "Saturday", "Sunday"] 
	


# def split_date(birthday): 


# 	year, month, day = birthday.split('-')	 
# 	return year, month, day 
	

# def get_birthday(birthday): 

# 	year, month, day = split_date(birthday) 

	
# 	bdate = datetime.datetime(int(year), int(month), int(day)) 


# 	weekday = bdate.weekday() 

	
# 	day = weekdays[weekday] 

# 	return day 


# def listToString(x): 

	
# 	String = " "

	
# 	return (String.join(x)) 


# def true_birthdays(birthdate): 
# 	year, month, day = split_date(birthdate) 


# 	year = birthdate[:4].split('-') 

	
# 	year = listToString(year) 

# 	d_day = get_birthday(birthdate) 

	 
# 	true_BD = [] 
	
# 	j = 0

# 	for i in range(int(year), 2050): 

		 
# 		new_year = int(year)+j 

	
# 		new_birthday = str(str(new_year)+"-"+month+"-"+day) 

	
# 		new_d_day = get_birthday(new_birthday) 

	
# 		if d_day == new_d_day: 

	
# 			true_BD.append(new_birthday) 
# 		else: 
# 			pass
# 		j += 1

# 	return true_BD 


# def main(): 

	
# 	birthdate = "1996-11-12"


# 	dates = true_birthdays(birthdate) 
	
# 	print(dates) 
	


# main() 



# import datetime


# def get_user_birthday():
#     year = int(input('When is your birthday? [YY] '))
#     month = int(input('When is your birthday? [MM] '))
#     day = int(input('When is your birthday? [DD] '))

#     birthday = datetime.datetime(year,month,day)
#     return birthday


# def calculate_dates(original_date, now):
#     date1 = now
#     date2 = datetime.datetime(now.year, original_date.month, original_date.day)
#     delta = date2 - date1
#     days = delta.total_seconds() / 60 /60 /24

#     return days


# def show_info(self):
#     pass



# bd = get_user_birthday()
# now = datetime.datetime.now()
# c = calculate_dates(bd,now)
# print(c)











# Task - 1

# from datetime import datetime

# def calculate_age(birth_date):

#     birth_datetime = datetime.strptime(birth_date, '%Y-%m-%d')
#     current_datetime = datetime.now()
    

#     age_timedelta = current_datetime - birth_datetime
#     years = age_timedelta.days // 365
#     months = (age_timedelta.days % 365) // 30
#     days = (age_timedelta.days % 365) % 30
#     hours = age_timedelta.seconds // 3600
#     minutes = hours * 60
#     seconds = age_timedelta.seconds % 3600
    
#     age = {
#         'years': years,
#         'months': months,
#         'days': days,
#         'hours': hours,
#         'minutes': minutes,
#         'seconds': seconds
#     }
    
#     return age
# if  "_main_":
#     birth_date = input("Enter your birth date in the format 'YYYY-MM-DD': ")
#     age = calculate_age(birth_date)
#     print ("You are {} years, {} months, {} days, {} hours,{} minutes and {} seconds old.".format( age['years'], age['months'], age['days'], age['hours'], age['minutes'], age['seconds']))






# Task - 3




# dict = {'num1': 2, 'num3' :3, 'num4': 4, 'num5': 5}

# a = dict.keys()

# print(choice(list(dict.values())))








# Task - 1




# name = input("Enter your name: ")

# while True:
#     print("\n(Select (1) List, (2) Dict, (3) Tuple, (4) Exit)")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         # List
#         data = input("Enter list data (comma-separated): ").split(',')
#         print("List:", data)
#     elif choice == '2':
#         # Dictionary
#         key = input("Enter key: ")
#         value = input("Enter value: ")
#         data = {key: value}
#         print("Dictionary:", data)
#     elif choice == '3':
#         # Tuple
#         data = input("Enter tuple data (comma-separated): ").split(',')
#         data_tuple = tuple(data)
#         print("Tuple:", data_tuple)
#     elif choice == '4':
#         print("Exiting program.")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")







# def get_user_choice():
#     options = {
#         '1': 'List',
#         '2': 'Dict',
#         '3': 'Tuple',
#         '4': 'Exit',
#     }

#     while True:
#         print("Select an option:")
#         for key, value in options.items():
#             print(f"{key}: {value}")

#         user_input = input("Enter the number of your choice: ")

#         if user_input in options:
#             return options[user_input]
#         else:
#             print("Invalid choice. Please try again.")

# # Example usage
# user_choice = get_user_choice()
# print(f"You selected: {user_choice}")




# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# d=dict()
# for line in handle:
#     if not line.startswith("From "): 
#         continue
#     else:    
#         line=line.split()
#         line=line[5]
#         line=line[0:2]
#         d[line]=d.get(line,0)+1

# lst=list()        
# for value,count in d.items():
#     lst.append((value,count))

# lst.sort()
# for value,count in lst:
#     print value,count








# Task - 3




# a = input("Enter:")

# b = int(input('Make are choise'))







# my_dict={}
# for items in range(1,4):
#     key=str(input('enter string'))
#     value=int(input('enter #'))
#     my_dict={f'{key}: {value}'}
#     print(my_dict)







# Task - 10

# Task - 1










# Task - 2



# def cube_generator(n):
#     for i in range(n+1, p):
#        yield i ** 3
       

# n = int(input("Enter number 1: "))
# p = int(input("Enter number 2:"))

# cubes = cube_generator(n)

# print("Cubes  from 1", n)
# for num in cubes:
#     print(num)






# def again():
#         c = 0  
#         a = int(input("a"))
#         if a >= 1:
#                 b = int(input("b"))
#                 while a and b >= 1:
#                         if b >= 1:
#                                 c += (a - b)
#                                 print("Result",c)
#                                 again()
#                                 break
#                         if a >= 0 and b >= 0:
#                                 break
# again()









# -----------------------------TASK-----------------------------



# import sqlite3

# data = sqlite3.connect('database.db')

# sql = data.cursor("")


# sql.execute("""CREATE IF NOT EXISTS TABLE data(
            
            
#             name VARCHAR(255)
            

#                 )""")


# # # sql.execute("INSERT INTO data(name) VALUES('orxan')")

# # sql.execute("SELECT * FROM data")


# # for x in sql.fetchmany(size=3):

# #     print (x)

# # print(sql)

# # # data.commit()





# # Printing the priority list
# print("Priority List:")
# for item in priority_list:
#     print(f"Request: {item.request}, Priority Level: {item.priority}")



# class Ucus():
#     havayolu = "THY"

#     def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):

#         self.kod = kod
#         self.kalkis = kalkis
#         self.varis = varis
#         self.sure = sure
#         self.kapasite = kapasite
#         self.yolcu = yolcu

# ucus2 = Ucus('TK123', 'IST', 'ANK', 60, 300, 50)

# ucus2.kalkis
# print(ucus2)


















# Task -  Səhiyyə Sənayesi Tapşırığı:


critical_list = ["cancer", "corona", "plague"]

class Patient:

   def __init__(self, name, age, health_status):
      
      self.name = name
      self.age = age
      self.health_staus = health_status


   def calculate_check (self):
      if self.age < 12 or self.health_staus in critical_list:

        return  "High priority"

      elif self.age >= 60:

        return "Medium"
      
      else:

        return "Low"
      

    patients = []
    for i in range(5):
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        health_status = input("Enter patient's health status: ")
       
        return patients










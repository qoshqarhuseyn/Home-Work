





# Task - 1 





# a = ["apple", "windows", "linux", "travel"]

# i = 0

# while i < len(a):
 
#   print(a[i])
  
#   i = i + 1




# Task - 2





# library = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

# i = 0
# while i < len(library):
#     if library[i] in ['c', 'g', 'i']:
#         i += 1
#         continue
#     print(library[i])
#     i += 1





# Task - 3


# a = int(input("Enter number"))

# b=0

# while b <= a:

#  print(b)
 
#  b+=1





# Task - 4




# userpassword = "Password123"

# for _ in range(3):
#     input_pass = input('Please enter password: ')
#     if input_pass == userpassword:
#         print('Thank you for providing the right password!')
#         break
# else:
#     print('Your account blocked!')




# Task - 5






# question1 = input("3*5=? a)15 b)20 c)10 ")
# question2 = input("4*5=? a)15 b)20 c)10 ")
# question3 = input("2*5=? a)15 b)20 c)10 ")
# question4 = input("5*5=? a)15 b)20 c)25 ")
# question5 = input("10*5=? a)50 b)20 c)10 ")
# question6 = input("3*3=? a)15 b)9 c)10 ")
# question7 = input("6*6=? a)15 b)36 c)10 ")
# question8 = input("3*2=? a)15 b)6 c)10 ")
# question9 = input("0*5=? a)15 b)0 c)10 ")
# question10 = input("3*1=? a)15 b)3 c)10 ")

# correct_answers = 0
# incorrect_answers = 0

# if question1 == "a":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question2 == "b":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question3 == "c":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question4 == "c":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question5 == "a":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question6 == "b":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question7 == "b":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question8 == "b":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question9 == "b":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if question10 == "b":
#     correct_answers += 1
# else:
#     incorrect_answers += 1

# if incorrect_answers % 4 == 0:
#     correct_answers -= 1

# print("Number of correct answers:", correct_answers)
# print("Number of incorrect answers:", incorrect_answers)











# Task 



def numbers (x):

    print(x)

    if x==20:
        return "day"
    
    return numbers(x-1)


       
print(numbers(30))

    
































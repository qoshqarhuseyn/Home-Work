

# Task - 1



# def budget_account (spent, profit):
#     remaining_budget = profit - spent
#     return remaining_budget

# def main():
#     spent = float(input("Enter total spent for the month: $"))
#     profit = float(input("Enter total profit for the month: $"))

#     remaining_budget = budget_account (spent, profit)

#     print("\nRemaining budget for the month: ${:.2f}".format(remaining_budget))

# main() 




 



# Task - 2


# height = float(input("Entre Your Height > "))
# weight = float(input("Entre Your Weight > "))

# bmi = weight / (height ** 2)

# if bmi < 16:
#     category = "Severely underweight"
# elif bmi <= 16.5:
#     category = "underweight"
# elif 17 <= bmi < 18.4:
#     category = "Mildly underweight"
# elif 18.5 <= bmi < 24.9:
#     category = "Normal"
# elif 25 <= bmi < 29.9:
#     category = "Overweight"
# elif 30 <= bmi < 34.9:
#     category = "Obesity class 1 (Moderate)"
# elif 35 <= bmi < 39.9:
#     category = "Obesity class 2 (Severe)"
# else:
#     category = "Obesity class 3 (Very severe or morbidly obese)"

# print("Your BMI is:", bmi)
# print("You are categorized as:", category)





# Task - 3





# def grade_feedback(average):
#     if average >= 91 and average <= 100:
#         return "A - Excellent!"
#     elif average >= 81 and average < 91:
#         return "A1 - Good!"
#     elif average >= 71 and average < 81:
#         return "B - Average!"
#     elif average >= 61 and average < 71:
#         return "B1 - Average!"
#     elif average >= 51 and average < 61:
#         return "C - Below Average!"
#     elif average >= 41 and average < 51:
#         return "C1- Below Average!"
#     elif average >= 33 and average < 41:
#         return "D - Below Average!"
#     elif average >= 21 and average < 33:
#         return "E - Satisfactory!"
#     elif average >= 0 and average < 21:
#         return "F - Satisfactory!"
#     else:
#         return "Invalid Input!"

# print("Enter Marks Obtained in 5 Subjects:")
# markOne = int(input("Biology: "))
# markTwo = int(input("Matematic: "))
# markThree = int(input("Physics: "))
# markFour = int(input("Music: "))
# markFive = int(input("Engilish: "))

# average = (markOne + markTwo + markThree + markFour + markFive) / 5


# print("Your Average Grade:", average)
# print("Feedback about Your Grade:", grade_feedback(average))
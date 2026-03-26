for i in range(1,11):
    print(i)

print("-"*30)
print("even number")
for i in range(1,11,2):
    print(i)
print("-"*30)
print("reverse")
for i in range(10,0,-1):
    print(i)
print("-"*30)
print("odd number")
for i in range(1,11,2):
    print(i)

for e in range(1,11):
    if e % 2 == 0:
        print(e)
for o in range(1,11):
    if o % 2 != 0:
        print(o)


name="Sajeeb"
for word in name:
    print(word)

list=["Europe", "Asia", "Africa", "North America", "South America"]
for country in list:
    print(country)
    for i in range(len(country)):
        print(f"{i}: {country[i]}")

employee={"name": "Sajeeb", "age": 24, "profession": "Data Analyst"}
for key in employee:
    print(key)
for key,value in employee.items():
    print(f"{key}: {value}")

for i in range(2,5):
    for j in range(3,6):
        print(f"{i} * {j} = {i*j}")
        print("-"*30)

# Namota
number=int(input("Enter a number:"))
print(f"Time table of {number}")
for i in range(1,11):
    result=number * i
    print(f"{number} * {i} = {result}")

numbers=[20,30,40,50,60]
total=0
for num in numbers:
    total+=num
average=total/len(numbers)
print(f"Total: {total}")
print(f"Average: {average}")

scores=[70,89,76,84,90,47]
max_score=scores[0]
min_score=scores[0]
for score in scores:
    if score > max_score:
        max_score=score
    if score < min_score:
        min_score=score
print(f"Maximum score: {max_score}")
print(f"Minimum score: {min_score}")

student={
    "Sajeeb":[88,90,77,46,69],
    "Sajid":[88,90,77,46,69],
    "Safia":[88,90,77,46,69],   
}
for name,scores in student.items():
    total=0
    for score in scores:
        total+=score
    average=total/len(scores)
    print(f"{name} average: {average}")

# ATM Withdrawl Menu
blance=float(input("Enter your blance: "))
while True:
    print("\n------------ ATM MENU -----------" )
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Blance")
    print("4. Exit")
    print("--" * 20)
    choice=int(input("Enter your choice (1-4): "))
    if choice == 1:
        amount=float(input("Enter the amount to withdraw: "))
        if amount > blance:
            print("Insufficient blance")
        else:
            blance-=amount
            print(f"You have withdrawn ${amount:,.2f}")
            print(f"Your blance is ${blance:,.2f}")
    elif choice == 2:
        amount=float(input("Enter the amount to deposit: "))
        blance+=amount
        print(f"You have deposited ${amount:,.2f}")
        print(f"Your blance is ${blance:,.2f}")
    elif choice == 3:
        print(f"Your blance is ${blance:,.2f}")
    elif choice == 4:
        break
    else:
        print("Invalid choice")

#grade analysis 
grades=[70,89,76,84,90,47,88,90,77,46,69]
print ("Grades Analysis")
print ("-" * 20)
print(f"Total number of grades: {len(grades)}")
exellent=0
good=0
average=0
poor=0
fail=0
for grade in grades:
    if grade >= 90:
        exellent+=1
    elif grade >= 80:
        good+=1
    elif grade >= 70:
        average+=1
    elif grade >= 60:
        poor+=1
    else:
        fail+=1
print(f"Number of excellent grades: {exellent}")
print(f"Number of good grades: {good}")
print(f"Number of average grades: {average}")
print(f"Number of poor grades: {poor}")
print(f"Number of fail grades: {fail}")

# Countdown Timer
import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Blast off")

import time
countdown=int(input("Enter the number of seconds: "))
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown-=1
print("Blast off")

# Validaation Loop
while True:
    age=input("Enter your age: ")
    if age.isdigit():
        age=int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
        break
    else:
        print("Invalid input")

#practice task --- Write a program that:
# - Asks user for a number
# - Prints times table from 1 to 10
# - Use a for loop

number=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

# Write a program that:
# - Asks user for how many numbers to add
# - Takes that many numbers as input
# - Calculates and prints sum and average

count = int(input("How many numbers do you want to add? "))

total = 0
for i in range(1, count + 1):
    number = float(input(f"Enter number {i}: "))
    total += number

average = total / count

print(f"Sum: {total}")
print(f"Average: {average}")

# Write a program that:
# - Loops from 1 to 50
# - Prints only odd numbers
# - Use continue to skip even numbers

for number in range(1, 51):
    if number % 2 == 0:
        continue
    print(number)

# Write a program that:
# - Repeatedly asks for password
# - Only accepts passwords with 8+ characters
# - Use while loop
# - Exit when correct password entered

password=""
while password != "correctpassword":
    password=input("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters")
        continue
    if password== "correctpassword":
        print("Login successful")
        break
    else:
        print("Incorrect password")

import random

target_number = random.randint(1, 100)
attempt = 1
max_attempts = 5

while attempt <= max_attempts:
    guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess (1-100): "))

    if guess == target_number:
        print("Correct! You guessed the number.")
        break
    elif guess < target_number:
        print("Too low.")
    else:
        print("Too high.")

    remaining = max_attempts - attempt
    print(f"Remaining attempts: {remaining}")
    attempt += 1

if attempt > max_attempts:
    print(f"Game over! The number was {target_number}.")

# Write a program that:
# - Loops through list of employees
# - Calculates total salary
# - Finds highest and lowest paid employee
# - Calculates average salary

employees = [
    {"name": "John", "salary": 50000},
    {"name": "Jane", "salary": 60000},
    {"name": "Bob", "salary": 40000},
    {"name": "Alice", "salary": 55000},
]
total_salary = 0
for employee in employees:
    total_salary += employee["salary"]

average_salary = total_salary / len(employees)

highest_paid = employees[0]
lowest_paid = employees[0]

for employee in employees:
    if employee["salary"] > highest_paid["salary"]:
        highest_paid = employee
    if employee["salary"] < lowest_paid["salary"]:
        lowest_paid = employee

print(f"Total salary: {total_salary}")
print(f"Highest paid employee: {highest_paid['name']} - {highest_paid['salary']}")
print(f"Lowest paid employee: {lowest_paid['name']} - {lowest_paid['salary']}")
print(f"Average salary: {average_salary}")

# Write a program that prints:
# ```
# *
# **
# ***
# ****
#  *****
for i in range(1,6):
    print("*"*i)

items=[]
while True:
    print("Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=input("Enter the item: ")
        items.append(item)
    elif choice==2:
        item=input("Enter the item to remove: ")
        if item in items:
            items.remove(item)
        else:
            print("Item not found")
    elif choice==3:
        print("Items:")
        for item in items:
            print(item)
    elif choice==4:
        print("Goodbye")
        break
    else:
        print("Invalid choice")

grades = []
while True:
    grade = int(input("Enter grade (-1 to exit): "))
    if grade == -1:
        break
    grades.append(grade)

histogram = ""
num_90_plus = 0
num_80_89 = 0
num_70_79 = 0
num_below_70 = 0

for grade in grades:
    if grade >= 90:
        num_90_plus += 1
    elif 80 <= grade <= 89:
        num_80_89 += 1
    elif 70 <= grade <= 79:
        num_70_79 += 1
    else:
        num_below_70 += 1

total_grades = len(grades)

histogram += f"90+: {'#' * num_90_plus}\n"
histogram += f"80-89: {'#' * num_80_89}\n"
histogram += f"70-79: {'#' * num_70_79}\n"
histogram += f"<70: {'#' * num_below_70}\n"

print("Histogram:")
print(histogram)
print("Total grades:", total_grades)

data = {}
while True:
    email = input("Enter email (format: name@domain.com): ")
    if "@" in email and email.split("@")[1].split(".")[0] != "":
        data["email"] = email
        break
    else:
        print("Invalid email format. Please try again.")

while True:
    age = input("Enter age: ")
    if age.isdigit():
        age = int(age)
        if age >= 0:
            data["age"] = age
            break
        else:
            print("Age must be a positive number. Please try again.")
    else:
        print("Invalid age. Please try again.")

while True:
    salary = input("Enter salary: ")
    if salary.isdigit():
        salary = int(salary)
        if salary > 0:
            data["salary"] = salary
            break
        else:
            print("Salary must be a positive number. Please try again.")
    else:
        print("Invalid salary. Please try again.")

print("Entered data:")
for key, value in data.items():
    print(key + ": " + str(value))
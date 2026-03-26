# x=10
# print(x==10)
# print(x!=10)
# print(x>10)
# print(x<10)
# print(x>=8)
# print(x<=7)

# age=21
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# name= "Sanjida"
# if name == "Sajeeb":
#     print("Hello Sajeeb")
# else:
#     print("Hello Sanjida")

# salary= 40000
# if salary >= 50000:
#     print("You are eligible for loan")
# else:
#     print("You are not eligible for loan")

# score=45
# if score >= 80:
#     print("I got A+")
# else:
#     print("Fail")

# marks= 75
# if marks>= 80:
#     print(" A+")
# elif marks >= 60:
#     print(" A")
# elif marks >= 40:
#     print(" B")
# else:
#     print("Fail")

# temperature= 30
# if temperature >= 30:
#     print("It is hot outside")
# elif temperature >= 20:
#     print("It is warm outside")
# elif temperature >= 10:
#     print("It is cool outside")
# else:
#     print("freezing")

# Logical Tempereture
# age=21
# has_license=True
# if age >= 18 and has_license:
#     print("You can drive")
# else:
#     print("You cannot drive")

# age=25
# salary=40000
# has_house=True
# if age>=25 and salary>=50000 or has_house:
#     print("You are eligible to marry her")
# else:
#     print("Go away")

# income=35000
# credit_score=700
# if income>=50000 and credit_score>=700:
#     print("You are eligible for loan")
# else:
#     print("You are not eligible for loan")


# marks= 80
# family_earning= 30000
# has_cycle= False
# if marks>= 80 and family_earning>= 50000 or has_cycle:
#     print("You can admit here")
# else:
#     print("You aren't worth of it")

# is_raining= True
# is_hot= True
# is_sunny= False
# if is_raining or is_hot or is_sunny:
#     print("You need an umbrella")
# else:
#     print("You don't need an umbrella")

# is_raining= False
# if not is_raining:
#     print("You don't need an umbrella")
# else:
#     print("You need an umbrella")

# is_student= False
# if not is_student:
#     print("You are not a student")
# else:
#     print("You are a student")

# age=25
# income=50000
# has_passport=True
# has_savings=False
# know_english=True
# know_spanish=False

# if age>=18 and income>= 45000 and has_passport and has_savings and know_english or know_spanish:
#     print("You are eligible to go Europe")
# elif age>=18 and income>= 45000 and has_passport or has_savings or know_english or know_spanish:
#     print("We can manage something but need to pay extra costs")
# else:
#     print("You don't desire to go Europe")

# nested conditionals
# age=25
# salary=25000
# if age>= 25:
#     if salary>= 50000:
#         print("You are eligible for loan")
#     else:
#         print("Your salary is too low")
# else:
#     print("You are not eligible for loan")

# exam_score= 75
# assignment_score= 80
# if exam_score >=80:
#     if assignment_score >= 80:
#         print("You passed with a good score")
#     else:
#         print("You passed with average score")
# else:
#     print("You failed")

# Ternary Operators
# age=21
# status="Adult" if age >= 28 else "Minor"
# print(status)

# score=45
# result= "Pass" if score >= 60 else "Fail"
# print(result) 

# number= int(input("Enter a number:"))
# result= "Even" if number % 2 == 0 else "Odd"
# print(result)

# Booleen Values

# is_active=False
# if is_active:
#     print("User is active")
# else:
#     print("User is not active")

# is_completed=False
# if is_completed:
#     print("Task is completed")
# else:
#     print("Task is not completed")

# name=""
# if name:
#     print("Name is not empty")
# else:
#     print("Name is empty")

# items=[]
# if items:
#     print("List is not empty")
# else:
#     print("List is empty")

# value=0
# if value:
#     print("Value is not empty")
# else:
#     print("Value is empty")

# data analysis
# salary=45000
# if salary<=20000:
#     category="Low Income"
# elif salary<=40000:
#     category="Middle Income"
# else:
#     category="High Income"
# print(category)

# age=121
# if age< 0:
#     print("Invalid age")
# elif age > 120:
#     print("Invalid age")
# else:
#     print("Valid age")

# score=43
# attendence=75
# if score >=80 and attendence >= 80:
#     print("Exellent performance")
# elif score >=70 and attendence >= 70:
#     print("Good performance")
# elif score >=60 and attendence >= 60:
#     print("Average performance")
# else:
#     print("Fail")

# value=[1,2,3,4,5]
# if isinstance(value, int):
#     print("Value is an integer")
# elif isinstance(value, float):
#     print("Value is a float")
# elif isinstance(value, str):
#     print("Value is a string")
# else:
#     print("Value is something else")

# number classifications 
# Write a program that takes a number and tells if it's:

# number= int(input("Enter a number:"))
# if number % 2 == 0:
#     parity= "Even"
# else:
#     parity= "Odd"

# if number >= 0:
#     status= "Positive"
# elif number <= 0:
#     status= "Negative"
# else:
#     status= "Zero"

# if -9 <= number <= 9:
#     range= "Single digit"
# else:
#     range= "Multi digit"

# print(f"The number{number} is {parity}, {status} and {range}")

# Write a program that takes a score (0-100) and assigns a grade:
# score= int(input("Enter a score:"))
# if score>=90:
#     grade= "A"
# elif score>=80:
#     grade= "B"
# elif score>=70:
#     grade= "C"
# elif score>=60:
#     grade= "D"
# else:
#     grade= "F"

# is_passing=score >=50
# status="Pass" if is_passing else "Fail"
# print(f"Your grade is {grade}")

# Write a program that checks if someone can vote. They must be:

# age=int(input("Enter your age:"))
# is_citizen= True
# is_registered= True
# if age >=18 and is_citizen and is_registered:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# age=int(input("Enter your age:"))
# is_citizen= input("Are you a citizen? (yes/no): ").lower() == "yes"
# is_registered= input("Are you registered? (yes/no): ").lower() == "yes"

# missing_requirements=[]
# if age<= 18:
#     missing_requirements.append("You are too young")
# if not is_citizen:
#     missing_requirements.append("You are not a citizen")
# if not is_registered:
#     missing_requirements.append("You are not registered")
# if not missing_requirements:
#     print("You are eligible to vote")
# else:
#     print(f"You are not eligible to vote. Missing requirements: {', '.join(missing_requirements)}")

# Write a program that calculates tax based on income
# salary=float(input("Enter your salary:"))
# if salary >=100000:
#     tax= salary * 0.3
#     actual_salary= salary - tax
# elif salary >=60000:
#     tax= salary * 0.2
#     actual_salary= salary - tax
# elif salary >=30000:
#     tax= salary * 0.15
#     actual_salary= salary - tax
# elif salary>=20000:
#     tax= salary * 0.1
#     actual_salary= salary - tax
# else:
#     tax=0
#     actual_salary= salary

# print(f"Your tax is {tax}")
# print(f"Your actual salary is {actual_salary}")

# salary=float(input("Enter your salary:"))
# if salary>= 100000:
#     tax_rate=0.3
# elif salary>= 60000:
#     tax_rate=0.2
# elif salary>= 30000:
#     tax_rate=0.15
# elif salary>= 20000:
#     tax_rate=0.1
# else:
#     tax_rate=0

# tax= salary * tax_rate
# actual_salary= salary - tax

# print(f"Tax Rate Applied:{tax_rate * 100}%")
# print(f"Your task is :${tax:,.2f}")
# print(f"Your actual salary is :${actual_salary:,.2f}")

# Write a program that takes weight (kg) and height (m) and calculates BMI:
# weight=float(input("Enter your weight in kg: "))
# height=float(input("Enter your height in m: "))
# BMI= weight / (height ** 2)
# if BMI < 18.5:
#     status= "Underweight"
# elif 18.5 <= BMI < 25:
#     status= "Normal"
# elif 25 <= BMI < 30:
#     status= "Overweight"
# else:
#     status= "Obese"

# print(f"Your BMI is {BMI:.2f} and you are {status}")

# weight_kg = 120
# height_ft = 5
# height_in = 2
# total_inches=(height_ft * 12) + height_in
# height_m = total_inches * 0.0254
# BMI = weight_kg / (height_m ** 2)
# if BMI < 18.5:
#     status = "Underweight"
# elif 18.5 <= BMI < 25:
#     status = "Normal"
# elif 25 <= BMI < 30:
#     status = "Overweight"
# else:
#     status = "Obese"

# print(f"Your BMI is {BMI:.2f} and you are {status}")

# Write a program that takes three subject scores and determines:
# physics_score= float(input("Enter physics score: "))
# chemistry_score= float(input("Enter chemistry score: "))
# biology_score= float(input("Enter biology score: "))
# average_score= (physics_score + chemistry_score + biology_score) / 3
# maximum_score= max(physics_score, chemistry_score, biology_score)
# minimum_score= min(physics_score, chemistry_score, biology_score)
# if average_score >= 80:
#     grade= "A"
# elif average_score >= 70:
#     grade= "B"
# elif average_score >= 60:
#     grade= "C"
# elif average_score >= 50:
#     grade= "D"
# else:
#     grade= "F"
# print(f"Average score: {average_score:.2f}")
# print(f"Maximum score: {maximum_score}")
# print(f"Minimum score: {minimum_score}")
# print(f"Grade: {grade}")

# math=float(input("Enter your math score: "))
# science=float(input("Enter your science score: "))
# english=float(input("Enter your english score: "))
# score= math + science + english
# average= score /3
# highest=max(math, science, english)
# lowest=min(math, science, english)
# status="Pass" if average >= 70 else "fail"
# is_distinction= all(s>=80 for s in [math, science, english])   
# print("--" * 20)
# print(f"Total Score: {score}")
# print(f"Average Score: {average}")
# print(f"Highest Score: {highest}")
# print(f"Lowest Score: {lowest}")
# print(f"Status: {status}")
# if is_distinction:
#     print("You have distinction")

# Write a program that validates a login with:
# username= input("Enter your username: ")
# pasword= input("Enter your password: ")
# error=[]
# if len(username) < 5:
#     error.append("Username must be at least 5 characters")
# if len (pasword) < 8:
#     error.append("Password must be at least 8 characters")
# if not error:
#     print("Login successful")
# else:
#     print("Login failed")
#     for err in error:
#         print(f"- {err}")

# Write a program that calculates discount based on purchase amount:
# price=float(input("Enter your price: "))
# if price > 10000:
#     discount= price * 0.2
#     axtual_price= price - discount
# elif price >= 5000 and price <=10000:
#     discount= price * 0.15
#     axtual_price= price - discount
# elif price >= 2000 and price <=5000:
#     discount= price * 0.1
#     axtual_price= price - discount
# else:
#     discount=0
#     axtual_price= price

# print(f"your discount is:${discount:,.2f}")
# print(f"your actual price is:${axtual_price:,.2f}")

# Write a program that takes a number (1-7) and prints the day:
# day= int(input("Enter a number between 1 and 7: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid input")
# if day >=1 and day <=5:
#     print("Weekday")
# elif day ==6 or day ==7:
#     print("Weekend")

# #Write a program that takes temperature in Celsius and:
# water_tempereture= float(input("Enter the water temperature in Celsius: "))
# fahrenheit= (water_tempereture * 1.8) + 32
# if water_tempereture < 0:
#     print("Freezing")
# elif water_tempereture >= 0 and water_tempereture < 15:
#     print("Cold")
# elif water_tempereture >=15 and water_tempereture < 35:
#     print("Warm")
# elif water_tempereture >=35 and water_tempereture < 100:
#     print("Hot")
# else:
#     print("Boiling")
# print (f"Temperature: {water_tempereture}°C ({fahrenheit:.1f}°F)")
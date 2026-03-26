#simple input
# name=input("Enter your name: ")
# print(name)
# print(type(name))
# age=input("Enter your age: ")
# print(age)
# print(type(age))

# first_name= input("What's your name ?")
# last_name= input("What's your last name ?")
# full_name= first_name + " " + last_name
# age= input("What's your age ?")
# profession= input("What's your profession ?")
# city=input("which city do you live in ?")
# print(f"I Live in {city}) and I am a {profession} and I am {age} years old")

# salary= int(input("What's your salary ?"))
# next_year_salary= salary * 1.05
# print(f"My salary is {salary} USD")
# print(f"My salary will increase by 5% and it will be {next_year_salary} USD")
# print(type(salary))

#type casting
# age=int(input("How old are you ?"))
# print(f"You are {age} years old")
# print(type(age))    

# birth_year= 2026- age
# print(f"You were born in {birth_year}")
# print(type(birth_year))

# from datetime import date
# birth_input = input("enter your birth date (YYYY:MM:DD):")
# birth_date = date.fromisoformat(birth_input)
# age = date.today() - birth_date
# print(f"You are {age.days // 365} years old")

# from datetime import date
# birth_input = input("enter your birth date (YYYY:MM:DD):")
# birth_date = date.fromisoformat(birth_input)
# today= date.today()
# age_years = today.year - birth_date.year
# age_months=(today.month - birth_date.month) + (today.day>=birth_date.day)
# age_days= (today - birth_date).days

# print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# from datetime import date
# birth_input = input("enter your birth date (YYYY:MM:DD):")
# birth_date = date.fromisoformat(birth_input)
# today=date.today()
# age_years = today.year - birth_date.year
# age_months = (today.month - birth_date.month) % 12
# age_days = (today - birth_date).days

# print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# from datetime import date

# birth_input = input("Enter your birth date (YYYY-MM-DD):")
# birth_date = date.fromisoformat(birth_input)

# today = date.today()
# age_years = today.year - birth_date.year
# age_months = (today.month - birth_date.month) if (today.month >= birth_date.month) else (today.month - birth_date.month + 12)
# age_days = (today - birth_date).days - (age_months * 30)

# print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# from datetime import date

# birth_input = input("Enter your birth date (YYYY-MM-DD):")
# birth_date = date.fromisoformat(birth_input)

# today = date.today()
# age_years = today.year - birth_date.year
# age_months = (today.month - birth_date.month) if (today.month >= birth_date.month) else (today.month - birth_date.month + 12)
# age_days = (today - birth_date).days - ((age_years * 365) + (age_months * 30))

# print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# from datetime import date

# birth_input = input("Enter your birth date (YYYY-MM-DD):")
# birth_date = date.fromisoformat(birth_input)

# today = date.today()
# age_years = today.year - birth_date.year
# age_months = (today.month - birth_date.month) if (today.month >= birth_date.month) else (today.month - birth_date.month + 12)
# age_days = (today - birth_date).days - ((age_years * 365) + (age_months * 30)) + 1

# print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

from datetime import date
from os import TMP_MAX

# birth_input = input("Enter your birth date (YYYY-MM-DD):")
# birth_date = date.fromisoformat(birth_input)

# today = date.today()
# age_years = today.year - birth_date.year
# age_months = (today.month - birth_date.month) if (today.month >= birth_date.month) else (today.month - birth_date.month + 12)
# age_days = (today - birth_date).days - ((age_years * 365) + (age_months * 30)) + 1

# if age_years == 0:
#     print(f"You are {age_months} months and {age_days} days old.")
# elif age_years == 1:
#     print(f"You are 1 year, {age_months} months, and {age_days} days old.")
# else:
#     print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# price="19.99"
# # price=float(price)
# print(price)
# print(type(price))

# price=10
# tax=0.07
# total_price= price + (price * tax)
# print("Total price is: ", total_price)

# quantity= 12
# price= 18.88
# total_price2= quantity * price
# # total_price= quantity * float(price)
# print("Total price is: ", total_price2)

# height= float(input("enter your height:"))
# next_height= height + 1
# print(f"next year your height will be: {next_height}")
# print(type(height))
# weight= input("enter your weight:")
# print("Your weight is: ", weight)
# print(type(weight)) 

# age=25
# print("I'm " + str(age) + " years old")

# print(bool(10))  
# print(bool(-10))
# print(bool(0))
# print(bool(""))
# print(bool("Sajeeb"))
# print(bool([1,2,3,4,5]))
# print(bool({"name": "Sajeeb"}))
# print(bool({" age": 0 })) 

# num ="20"
# print(num)
# print(type(num))
# num= int(num)
# num +=10
# print(num)
# print(type(num))

# temperature= "33.34"
# print(temperature)
# print(type(temperature))
# temperature= float(temperature)
# temperature +=10
# print(temperature)
# print(type(temperature)) 

# basic calculations
# num=int(input("enter a number as first number"))
# num2=int(input("enter a number as second number"))
# addidtions= num + num2
# subtraction= num - num2
# multiplication= num * num2
# division= num / num2
# floor_division= num // num2
# module= num % num2
# exponentiation= num ** num2
# print(f"addition is {addidtions}") 
# print(f"subtraction is {subtraction}")
# print(f"multiplication is {multiplication}") 
# print(f"division is {round(division,2)}") #round(division}") 
# print(f"floor division is {floor_division}") 
# print(f"exponentiation is {exponentiation}")

## total value

# num1=float(input("enter a number as first number"))
# num2=float(input("enter a number as second number"))
# sum_result= num1 + num2
# diffrence= num1 - num2
# product= num1 * num2
# quiotent= num1 / num2
# print(f"\ncalculations for {num1} and {num2}")
# print(f"sum is {sum_result}")
# print(f"diffrence is {diffrence}")
# print(f"product is {product}")
# print(f"quotient is {round(quiotent,2)}")

# price=float(input("price per unit"))
# quantity=float(input("quantity"))
# total= price * quantity
# print(f"price per unit: ${price}")
# print(f"quantity: {quantity}")
# print(f"total: ${total}")

## Average Price

# market= {
# "tometos_price": float(input("enter tometos price:")),
# "tomatoes_quantity":float(input("enter tomatoes quantity: ")),
# "eggs_price": float(input("enter eggs price: ")),
# "eggs_quantity": float(input("enter eggs quantity: ")),
# "apples_price": float(input("enter apples price: ")),
# "apples_quantity": float(input("enter apples quantity: "))

# }

# average_price= (round(market["tometos_price"] + market["eggs_price"] + market["apples_price"],2)) / 3
# total_quantity= market["tomatoes_quantity"] + market["eggs_quantity"] + market["apples_quantity"]
# print(f"Average price: ${average_price}")
# print(f"Total quantity: {total_quantity}")

## Temperature Conversion

# celsius= float(input("enter temperature in celsius"))
# fahrenheit= (celsius * 1.8) + 32
# print(f"{celsius} celsius is equal to {fahrenheit} fahrenheit")

# fahrenheit= float(input("enter temperature in fahrenheit"))
# celsius= (fahrenheit - 32) / 1.8
# print(f"{fahrenheit} fahrenheit is equal to {celsius} celsius")

## Calculate Discount
# original_price= float(input("Enter the original price: "))
# discount_percentage= float(input("Enter the discount percentage: "))
# discount_amount= original_price * (discount_percentage / 100)
# discounted_price= original_price - discount_amount
# print(f"Original Price: ${original_price}")
# print(f"Discount Percentage: {discount_percentage}%")
# print(f"Discount Amount: ${discount_amount}")
# print(f"Discounted Price: ${discounted_price}")

#calculate age
# present_year= int(input("Enter the present year: "))
# birth_year= int(input("Enter the birth year: "))
# age= present_year - birth_year
# print(f"You are {age} years old.")

# area and perimeters calculators
# length= float(input("Enter the length: "))
# width= float(input("Enter the width: "))
# area= length * width
# perimeter= 2 * (length + width)
# print(f"\nTectangle dimension: {length} x {width}")
# print(f"Area: {area}")
# print(f"Perimeter: {perimeter}")

# import math
# radius=float(input("Enter the radius: "))
# area= math.pi * radius ** 2
# circumference= 2 * math.pi * radius
# print(f"Radius: {radius}")
# print(f"Area: {area}")
# print(f"Circumference: {circumference}")

# billing system 
# name=input ("Enter customer name: ")
# product_name=input("Enter product name: ")
# product_price=float(input("Enter product price: "))
# product_quantity=int(input("Enter product quantity: "))
# tax_rate= float(input("Enter tax rate (%): "))
# subtotal= product_price * product_quantity
# tax= subtotal * (tax_rate / 100)
# total= subtotal + tax
# print("\n" + "="*30)
# print(f"Customer Name: {name}")
# print(f"Product Name: {product_name}")
# print(f"Product Price: ${product_price}")
# print(f"Product Quantity: {product_quantity}")
# print(f"Tax Rate: {tax_rate}%")
# print(f"Subtotal: ${subtotal}")
# print(f"Tax: ${tax}")
# print(f"Total: ${total}")

#BMI Calculator
# weight=float(input("Enter your weight (kg): "))
# height=float(input("Enter your height (m): "))
# BMI= weight / (height ** 2)
# print(f"Your BMI is: {BMI}")

# customer_name = input("Enter customer name: ")
# quantity = int(input("Enter quantity: "))
# price_per_item = float(input("Enter price per item: "))
# tax_rate = float(input("Enter tax rate (%): "))

# subtotal = quantity * price_per_item
# tax_amount = subtotal * (tax_rate / 100)
# total = subtotal + tax_amount

# print("\n" + "="*30)
# print("BILL")
# print("="*30)
# print(f"Customer: {customer_name}")
# print(f"Quantity: {quantity}")
# print(f"Price per item: ${price_per_item}")
# print(f"Subtotal: ${subtotal}")
# print(f"Tax ({tax_rate}%): ${tax_amount}")
# print(f"Total: ${total}")
# print("="*30)

#Salary Calculatioins
# name=input("Enter employee name: ")
# hourly_rate=float(input("Enter hourly rate: "))
# hours_worked=float(input("Enter hours worked: "))
# tax=float(input("Enter tax rate (%): "))
# gross_pay= hourly_rate * hours_worked
# tax_amount= gross_pay * (tax / 100)
# net_pay= gross_pay - tax_amount
# print("\n" + "="*30)
# print("PAYSLIP")
# print("="*30)
# print(f"Employee Name: {name}")
# print(f"Gross Pay: ${gross_pay}")
# print(f"Tax: ${tax_amount}")
# print(f"Net Pay: ${net_pay}")
# print("="*30)

# price=199.971
# print(round(price,2))
# print(f"{price:.2f}")

# total=9460.872
# print(round(total,2))
# print(f"${total:.2f}")

# percentage= 0.85
# print(f"{percentage:.1%}")

# big_number=1000000
# print(f"{big_number:,}")

print("="*30)
print("Simple calculator")
print("="*40)

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

add=num1+num2
substract=num1-num2
multiply=num1*num2
divide=num1/num2 if num2 !=0 else "Cannot divide by zero"
modulo=num1%num2 if num2 !=0 else "Cannot divide by zero"
print("\n" + "="*30)
print(f"Addition: {num1} + {num2} = {add}")
print(f"Subtraction: {num1} - {num2} = {substract}")
print(f"Multiplication: {num1} * {num2} = {multiply}")
print(f"Division: {num1} / {num2} = {divide}")
print(f"Modulo: {num1} % {num2} = {modulo}")
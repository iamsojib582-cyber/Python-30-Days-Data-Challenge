condition= True
condition2= False
if condition:
    if condition2:
        print("Both conditions are true")
    else:
        print("First condition is true")
else:
    print("First condition is false")

age=int(input("Enter your age:"))
has_passport=input("Do you have a passport:")
if age >=18:
    if has_passport:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
else:
    print("You must be 18 years old")

score=70
attendence=86
if score >= 70:
    if attendence >= 80:
        print("you pass with high attendance")
    else:
        print("you pass but low attendance")
else:
    if attendence >= 90:
        print("you fail but high attendance")
    else:
        print("you fail and improve both score and attendance")

age=25
salary=45000
credit_score=700
has_house=True
if age >=24:
    if salary>=40000:
        if credit_score>=700:
            if has_house:
                print("You can get loan imedietly")
            else:
                print("You must have a house to get loan")
        else:
            print("You must have good credit score to get loan")
    else:
        print("You must have good salary to get loan")
else:
    print("You must be 24 years old to get loan")

score=70
bonus_points= 7
if score >80:
    if bonus_points>10:
        final_grade="A+"
    elif bonus_points>5:
        final_grade="A"
    else:
        final_grade="A-"
elif score >=70:
    if bonus_points> 10:
        final_grade="B+"
    else:
        final_grade="B"
else:
    final_grade="C"
print(f"final_grade: {final_grade}")

username="Sajeeb1920"
password="England1920"
is_active=True
is_verified= False
if username=="Sajeeb1920":
    if password=="England1920":
        if is_active:
            if is_verified:
                print("Login successful")
                print("Welcome Sajeeb")
            else:
                print("Your account is not verified")
        else:
            print("Your account is not active")
    else:
        print("Incorrect password")
else:
    print("User name is not found")

pin_correct=True
account_locked=False
blance=10000
withdraw_amount=7000
daily_limit=20000
if pin_correct:
    if not account_locked:
        if blance>=withdraw_amount:
            if withdraw_amount<=daily_limit:
                blance-=withdraw_amount
                print("Withdrawal successful")
                print(f"Your new balance is {blance}")
            else:
                print("you have exceeded your daily limit")
        else:
            print("Insufficient balance")
    else:
        print("Your account is locked")
else:
    print("Incorrect pin")

red_light=False
yellow_light=False
pedestrian_crossing=False
emergency_vehicle=True
if emergency_vehicle:
    print("Clear the Road")
else:
    if red_light:
        if pedestrian_crossing:
            print("Stop")
        else:
            print("Stop and wait")
    elif yellow_light:
        if pedestrian_crossing:
            print("Stop")
        else:
            print("Slow down")


# Practice task from here 
#Write a program that checks:

# If age >= 65: Senior discount (20%)
# If has membership card: Member discount (15%)
# If is student with valid ID: Student discount (15%)

price=float(input("Enter the price of the item: "))
age=int(input("Enter your age: "))
has_membership_card=input("Do you have a membership card? (yes/no): ").lower() == "yes"
is_student=input("Are you a student? (yes/no): ").lower() == "yes"
valid_student_id=input("Do you have a valid student ID? (yes/no): ").lower() == "yes"
if age >=65:
    discount=0.20
    reason="Senior discount"
elif has_membership_card:
    discount=0.15
    reason="Member discount"
elif is_student and valid_student_id:
    discount=0.15
    reason="Student discount"
else:
    discount=0
    reason="No discount"
discount_amount=price * discount
actual_price=price - discount_amount
print(f"Original Price: ${price:,.2f}")
print(f"Discount Reason: {reason}")
print(f"Discount Amount: ${discount_amount:,.2f}")
print(f"Actual Price: ${actual_price:,.2f}")

#Game Level Access
unlocked_prev=input("Have you unlocked the previous level? (yes/no): ").lower() == "yes"
score=int(input("Enter your score: "))
lives=int(input("Enter the number of lives: "))
if unlocked_prev and score>=80 and lives>0:
    print("You can access the next level")
    print("Welcome to the next level")
else:
    print("You cannot access the next level")
    print("Better luck next time")
if not unlocked_prev:
    print("You must unlock the previous level first")
if score<80:
    print("You need to improve your score")
if lives==0:
    print("You need to buy more lives")

#Movie Ticket Price
ticket_price=float(input("Enter the ticket price: "))
movie_rated=input("Enter the movie rating (G, PG, PG-13, R): ").upper()
age=int(input("Enter your age: "))
has_gurdian=input("Do you have a guardian? (yes/no): ").lower() == "yes"
is_student=input("Are you a student? (yes/no): ").lower() == "yes"
can_watch=True
if movie_rated=="G":
    if age>=18:
        can_watch=True
    elif age<18 and has_gurdian:
        can_watch=True
    else:
        can_watch=False
if not can_watch:
    print("You cannot watch this movie")
else:
    if age < 12:
        discount=0.50
        category="Kid"
    elif age>=65:
        discount=0.25
        category="Senior"
    elif is_student:
        discount=0.10
        category="Student"
    else:
        discount=0
        category="Adult"
    discount_amount=ticket_price * discount
    actual_price=ticket_price - discount_amount
    print(f"Ticket Price: ${ticket_price:,.2f}")
    print(f"Ticket Category: {category}")
    print(f"Discount Amount: ${discount_amount:,.2f}")
    print(f"Actual Price: ${actual_price:,.2f}")

# Bank Transaction
items_in_stock=True
payment_method=input("Enter the payment method (cash/credit): ").lower()
items_price=float(input("Enter the item price: "))
quantity=int(input("Enter the quantity: "))
total_price=items_price * quantity
if not items_in_stock:
    print("Items are out of stock")
elif total_price < 100:
    print("You must pay the full amount")
else:
    if payment_method=="cash":
        change=total_price - 100
        print(f"Your change is ${change:,.2f}")
    else:
        print("Thank you for your purchase")

# Employee Promotions
Years_of_service=int(input("Enter the years of service: "))
performance_ratings= float(input("Enter the performance ratings: "))
salary=float(input("Enter the salary: "))
available_position=True
manager_approval=True
if Years_of_service >=3:
    if performance_ratings>= 4.5:
        if salary>=50000:
            if available_position:
                if manager_approval:
                    new_salary= salary* 1.15
                    print(f"You are promoted. Your new salary is ${new_salary:,.2f}")
                else:
                    print("Manager approval is required")
            else:
                print("There is no available position")
        else:
            print("Your salary is not high enough")
    else:
        print("Your performance ratings are not high enough")
else:
    print("Your years of service are not enough")

Years_of_service=int(input("Enter the years of service: "))
performance_ratings= float(input("Enter the performance ratings: "))
salary=float(input("Enter the salary: "))
available_position=True
manager_approval=True
if Years_of_service >=3 and performance_ratings>= 4.5 and salary>=50000 and available_position and manager_approval:
    new_salary= salary* 1.15
    print(f"You are promoted. Your new salary is ${new_salary:,.2f}")
else:
    print("You are not promoted")
if Years_of_service < 3:
    print("Your years of service are not enough")
if performance_ratings < 4.5:
    print("Your performance ratings are not high enough")
if salary < 50000:
    print("Your salary is not high enough")
if not available_position:
    print("There is no available position")
#arithmetic operators
a=17
b=3
addition= a + b
subtraction= a - b
multiplication= a * b
division= round(a / b,2)
floor_division= a // b
modulus= a % b
exponentiation= a ** b
power= a ** 2
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
print("Floor Division: ", floor_division)
print("Modulus: ", modulus)
print("Exponentiation: ", exponentiation)
print("Power: ", power)

#comparison operators

a=10
b=6
print("Is a equal to b? ", a == b)
print("Is a not equal to b? ", a != b)
print("Is a greater than b? ", a > b)
print("Is a less than b? ", a < b)
print("Is a greater than or equal to b? ", a >= b)
print("Is a less than or equal to b? ", a <= b)

x=22
y=14
z=22
s=24
addition= x + y
addition2= y+ z
addition3= z + s
substraction= s - y
substraction2= z - x
substraction3= y - s
multiplication= x * y
multiplication2= y * z
multiplication3= z * s
division= x / y
division2= z / x
division3= s / y
floor_division= x // y
floor_division2= z // x
floor_division3= s // y
modulus= x % y
modulus2= z % x
modulus3= s % y
exponentiation= x ** 2
exponentiation2= y ** 2
exponentiation3= z ** 2
print("is addition 1 is greater than addition 2? ", addition > addition2)
print("is addition 1 is less than addition 3? ", addition < addition3)
print("is division 1 is equal to division 2? ", division == division2)
print("is division 1 is not equal to division 3? ", division != division3)
print("is substraction 1 is less than substraction 2? ", substraction < substraction2)
print("is multiplication 1 is equal to multiplication 2? ", multiplication == multiplication2)
print("is modulus 1 is greater than modulus 2? ", modulus > modulus2)
print("is exponentiation 1 is less than exponentiation 3? ", exponentiation < exponentiation3)
print("is floor division 2 is not equal to floor division 3? ", floor_division2 != floor_division3)
print("is multiplication 3 is greater than multiplication 1? ", multiplication3 > multiplication)
print("is substraction 3 is less than substraction 1? ", substraction3 < substraction)
print("is addition 2 is equal to addition 3? ", addition2 == addition3)
print("is exponentiation 2 is not equal to exponentiation 1? ", exponentiation2 != exponentiation)

print("is floor division 1 is greater than floor division 3? ", floor_division > floor_division3)
print("is modulus 3 is less than modulus 1? ", modulus3 < modulus)
print("is division 2 is equal to division 3? ", division2 == division3)
print("is substraction 2 is not equal to substraction 3? ", substraction2 != substraction3)
print("is addition 3 is greater than addition 2? ", addition3 > addition2)
print("is multiplication 2 is less than multiplication 3? ", multiplication2 < multiplication3)
print("is exponentiation 3 is equal to exponentiation 2? ", exponentiation3 == exponentiation2)
print("is modulus 2 is not equal to modulus 3? ", modulus2 != modulus3)
print("is floor division 3 is greater than floor division 1? ", floor_division3 > floor_division)    
print("is division 3 is less than division 1? ", division3 < division)                  

name1="Sajeeb"
name2="Sanzida"
print("Are the two names equal? ", name1 == name2)
print("Are the two names not equal? ", name1 != name2)
print("Is name1 greater than name2? ", name1 > name2)
print("Is name1 less than name2? ", name1 < name2)

#Logical Operators
name="Sajeeb"
age=25
salary=50000
print("Is age greater than 18 AND salary greater than 40000? ", age > 18 and salary > 40000)
print("Is age less than 18 OR salary greater than 40000? ", age < 18 or salary > 40000)
print("Is NOT age greater than 18? ", not(age > 18))

# print("He is perfect for you")
# if age>=21 and salary>=30000:              
#         print("You can marry him")
# else:
#         print("You cannot marry him")

# x=20
# y=19.50
# z=21
# print((x>y)and (y<z)) 
# print ((x==y)and (y!=z)) 

#assignment operators
# x=5
# print(x)    
# x +=3 
# print(x) 
# x -=3
# print(x) 
# y=10
# y /=2
# print(y)
# print(x*y)
# print
# x //=3 
# print(x)

# name="Sajeeb"
# name += " khan"
# salary= 40000
# salary *= 1.10
# tax= salary* 0.10
# print(tax) 
# family_portion= salary/ 4
# print(name)
# print(salary)
# print("Family will get:",family_portion)

# price= 84
# price *= 0.10
# print(price)
# price2=  100
# price2= price2 * 0.9
# print(price2) 

# salary=20000
# salary2= salary * 0.10
# salary *=1.10
# print(salary2)
# print(salary)

#Membership Operators
# fruits=["apple", "banana", "orange"]
# print("apple" in fruits)
# print("mango"not in fruits) 
# print("grape" in fruits)

# numbers=[1,2,3,4,5]
# print(1 in numbers)
# print(6 in numbers)
# print(7 not in numbers)

# text= "Python"
# print("P"in text)
# print("z" in text)

# details= {
#     "name": "Sajeeb",
#     "gender": "Male",
#     "age": 21
# }
# print("name" in details)
# print("marital_status" in details)
# print("class" not in details)

# Identity operators
a=[1,2,3,4]
b=[2,3,4]
c=a
print(a is b) 
print(c is a)

x="Sajeeb"
y="Monni"
c= x+y
print(x is y) 
print("Sajeeb" in c and "Monni" in c)

name= "Sajeeb"
name2=name
print(name is name2)
print(name==name2)

#Operator Precedece
result= (10+5) * 5
print(result)

marks=10+5 * 5
print(marks)

orders=3+2 **2
print(orders)

orders=(3+2) **2
print(orders)
print( 20 > 15 and 25<20)

original_price= 100
discount_percentage=20
final_price= original_price * (1- discount_percentage / 100)
print(f"final_price: ${final_price}")

number= 17
is_even = (number % 2== 0)
is_positive= (number>0)
print(f"Even and positive: {is_even and is_positive}")

age=25
salary= 50000
has_credit= False
can_get_loan= (age >=20) and (salary > 40000 and has_credit)
print(f"can_get_loan: {can_get_loan}")

num= 70
in_range= (num >= 0) and (num <= 79)
print(f"The number is: {in_range}")

age=25
print(0< age <100)
print(0> age > 100)

marks= 85
print(80 <= marks <= 100)

score = 82.5
if score >= 80:
    print("I got A+")
else:
    print("Fail") 

#practice task 
hourly_rate= 25
worked_hour= 40
tax_percentage= 15
comission= 20
per_day_work_hour= worked_hour / 7
gross_salary= hourly_rate * worked_hour
take_home= gross_salary* (1-tax_percentage / 100)
total_salary= take_home * 1.2 
print(f"Days_time: {round(per_day_work_hour,2)}")
print(f"gross_salary: {gross_salary}")
print(f"take_home_with_tax: ${take_home}")
print(total_salary) 

age=30
experience= 5
certifications= True
eligible= (age>= 25) and (experience>= 3 or certifications)
print(f"Job_eligible: {eligible}")
   
score = 75
print(f"Passing grade (60-80):{60<= score <=100}")

#dictionaries 

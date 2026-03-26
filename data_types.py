# # # ## data types in python\
# # # # # strings

name = "Sajeeb"
message = 'Hello, World!'
multiline_message = "He Sanida , I Love You"
print(name)
print(message)
print(multiline_message)
print(type(name))

# #strings operations
greeting = "Hello"
first_name= "Sajeeb"
last_name= "Nami"
full_name= first_name + " " + last_name
called_name= greeting + ", " + full_name
repeated_greeting= greeting  * 3
print(first_name)
print(last_name)
print(full_name)
print(called_name)
print(repeated_greeting)
print(type(full_name))
print(type(greeting))
print(len(full_name))
print(text := "Length of full_name is " + str(len(full_name)))
print(first_name[0])
print(last_name[-1])

# name= "Sajeeb"
# print(name[0])
# name= {"first_name": "Sajeeb",
#     "last_name": "Khan",
#     "age": 25
# } 
# print(name) 

# name= "sajeeb"
# print (name.upper())
# print(name.capitalize())    
# print(name.replace("s", "X"))

# sentence= "Hello, my name is sajeeb. I am learning python. Python is fun."
# print(sentence.count("is"))
# print(sentence.find("sajeeb"))
# print(sentence.replace("python", "Java"))
# print(sentence.split(".")) 

# # integers
# age=25
# temperature=-10
# year=2024
# big_number=12345678901234567890
# print(age)
# print(temperature)
# print(year)
# print(big_number)
# print(type(age))
# print(type(temperature))
# print(type(year))
# print(age +1)
# print(temperature -5)
# print(year +2)

# x= 75
# y = 24
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** 2)
# print(pow(x, 2))
# print(abs(-x))
# print(round(3.14159, 2))
# print(min(x, y))
# print(max(x, y)) 
   
# # # # floating-point numbers
# price=19.99
# tax=0.07
# total_price= price + (price * tax)
# print("Total price is: ", total_price) 
# print(type(price))
# print(type(tax))
# print(round(total_price, 2))
# # print(float(10))
# price= "19.99"
# temp= "23.5"
# percentage= "85.6"
# print(float(price) + float(temp) + float(percentage))
# print(type(float(price)))
# print(type(float(temp)))

# x=13.5
# y=2.3
# print(x + y)
# print(x - y)
# print(round(x * y),2)
# print(round(x / y),2)
# print(x // y)
# print(round(x % y),2)
# print(x ** 2)
# print(type(x))
# print(round(x, 1))
# print(abs(-x))

# does_love=True
# does_not_love=False
# print(does_love)
# print(does_not_love)
# print(type(does_love))
# print(type(does_not_love))
# print(does_love and does_not_love)
# print(does_love or does_not_love)
# print(not does_love)
# print(not does_not_love)
# print(f"Does love: {does_love}, Does not love: {does_not_love}")

# x=10
# y=6
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)
# print(f"x is {x} and y is {y}.")

# #list Variables
# # remember lists are mutable (can be changed)

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
print(type(numbers))
numbers.insert(0, 5)
print(numbers)
numbers.remove(30)
print(numbers)
last_number = numbers.pop()
print("Popped number: ", last_number)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
numbers.clear()
print(numbers)
print(f"Numbers List: {numbers}")

# # tuples variables
# #tuples are immutable (cannot be changed)

series = ("Money Heist", "Breaking Bad", "Stranger Things")
print(series)
print(type(series))
print(series[0])

#series This will raise an error because tuples are immutable
print(series)

# #dictionaries variables
#dictionaries are mutable (can be changed)
person = {
    "name": "Sajeeb",
    "age": 25,
    "city": "New York"
}
print(person)
print(type(person))
print(person["name"])
person["age"] = 26
print(person)
person["profession"] = "Data Analyst"
print(person)
del person["city"] 
print(person)
print(f"My name is {person['name']}, I am {person['age']} years old and I work as a {person['profession']}.")

student={"name":"Sajeeb", "age":25, "city":"New York"}
print(student["name"])
print(student["age"])
student["subjects"]= ["Math", "Science", "English"]
student["city"]= "Los Angeles"
print(student) 
del student["age"]
print(student)
print("age" in student)
print(student.keys()) 
print(student.values())
print(f"Student Info: {student}")

# #sets variables
# # sets are mutable (can be changed) and unordered collections of unique elements

age={25, 30, 35, 40, 25, 30}
print(age)
print(type(age))
age.add(45)
print(age)
age.remove(30)
print(age)
print(sorted(age))
print(25 in age)
print(50 in age)
print(f"Age Set: {age}")

a= {1, 2, 3, 4, 5}
b= {4, 5, 6, 7, 8} 
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(f"Set A: {a}, Set B: {b}")

# #type conversion
num_str= "100"
num_int= int(num_str)
num_float= float(num_str)
print(num_str)
print(num_int)
print(num_float)
print(type(num_str))
print(type(num_int))
print(type(num_float))
print(num_int + 50)
print(num_float + 50.5)
print(num_str + "50")

print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(""))

print(bool("Hello"))
print(bool(" "))

######### Practice Variables and Data Types ###########################

first_name ="Mosaddek Hosen"
last_name ="Sajeeb"
age=25
height=5.9
profession="Data Analyst"
home_town=("Peerganj", "Rangpur", "Bangladesh") 
prsent_adress={
    "city": "Dhaka",
    "area": "Banani",
    "road" : "11A",
    "region" : "North"
}
hobbies=["Watching Movies", "Traveling", "Coding", "Listening to Music"]
contact_info={
    "email": "martinsajeeb2001@outlook.com",
   "phone_number": "+8801234567890"
}
salary=50000
salary_next_year= salary * 1.05
is_employee=True
print("Employee Name: ", first_name+ " " +last_name)
print("employee_age:", age)
print("Employee Height:", height, "feet")
print("Profession:", profession)
print("Hometown:", home_town)
print("Present Address:", prsent_adress)
print("Hobbies:", hobbies)
print("Contact Info:", contact_info)
print("Current Salary:", salary, "USD")
print("Salary Next Year:", salary_next_year)
print("Is Employee:", is_employee)
print(f"{first_name} {last_name} is a {age} years old {profession} from {prsent_adress['city']}, {prsent_adress['region']}. He enjoys {hobbies[0]}, {hobbies[1]}, and {hobbies[2]}. You can contact him via email at {contact_info['email']}. His current salary is {salary} USD, and next year it will increase by 5%. Is he an employee? {is_employee}.")

print(type(first_name))
print(type(age))
print(type(height))
print(type(profession))
print(type(home_town))
print(type(prsent_adress))
print(type(hobbies))
print(type(contact_info))
print(type(salary))
print(type(is_employee))

#dictionaries
name="Sajeeb"
print(name)
print(type(name))
name="Sajeeb"
profession="Data Analyst"

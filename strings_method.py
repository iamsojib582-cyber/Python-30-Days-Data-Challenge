# name='Sajeeb'
# message="Hello, World!"
# text="""this is 
# a one of the 1920
# multiline text"""
# strings=name + " " + message
# print(strings)
# print(text)
# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[0:5])
# print(name[0:7:2])

# Strings Slicing 
# text="python"
# print(text[0])
# print(text[1])
# print(text[-1])
# print(text[-3])

# print(text[:2])
# print(text[3:])
# print(text[:])
# print(text[2:5])
# print(text[1:-1])
# print(text[::2])  
# print(text[-1:3:-1]) 

# #String Length 
# text="Hello, Monni. Good Morning"
# print(len(text))
# print("Monni" in text)
# print("Sanzida" in text)
# print("Sanzida" not in text)
# print("s" in text)

# text="my name is sajeeb"
# print(text.upper())

# country="england"
# print(country.upper())

# name="MONNI"
# print(name.lower())

# gmail="IAmSojib582@GMail.com"
# print(gmail.lower())

# name= "martin sajeeb"
# print(name.capitalize())

# name2="Sanzida sultana rifaa"
# print(name2.capitalize())

# name= "martin sajeeb"
# name2="Sanzida sultana rifaa"
# print(name.title())
# print(name2.title())

# text="     hey sanzida   , i love   " \
# "     you     " 
# print(text)
# print(text.strip())

# words=text.split()
# clean_text=" ".join(words)
# print(clean_text)

# print(text.rstrip())
# print(text.lstrip())
# print(text.strip())

# text="*****Hello, Sanzida*****"
# print(text.strip("*"))

# text="Hello, Sanzida"
# print(text)
# print(text.replace("Hello", "Bonjour"))
# print(text.replace("Sanzida", "Monni"))
# print(text.replace("Hello", "Bonjour").replace("Sanzida", "Monni"))

# text="My name is Sajeeb. My favourite anime is 'One Piece'"
# print(text)
# print(text.replace("Sajeeb","Martin"))
# print(text.replace("One Piece", "Naruto"))
# print(f"{text.replace('Sajeeb', 'Martin').replace('One Piece', 'Naruto')}")

# text="aba"
# print(text.replace("a", "b"))
# print(text.replace("a", "b", 1))
# print(text.replace("a", "b", 2))

# text="Monni Sajeeb Sanzida"
# words=text.split()
# print(words)

# row_data="Sajeeb, 21, Male"
# name, age, gender=row_data.split(",")
# print(name)
# print(age)
# print(gender)

# text="a-b-c-d"
# words=text.split("-",2)
# print(words)

# text=['monni', 'sajeeb', 'sanzida']
# upper_case_text=[name.upper() for name in text]
# text2="-".join(upper_case_text)
# print(text2)

# items=["apple", "banana", "cherry"]
# upper_case_items=[item.upper() for item in items]
# print(upper_case_items)

# text="Hello, Sanzida"
# print(text.find("Sanzida"))
# print(text.find("San"))
# print(text.find("xyz"))
# print(text.rfind("Sanzida"))
# print(text.rfind("San"))
# print(text.rfind("xyz"))
# print(text.find("San") != -1)

# text="Hello world, hellow Python"
# print(text.count("ello"))
# print(text.count("o"))

# text="Hello world, hellow Python"
# print(text.startswith("Hello"))
# print(text.startswith("hello"))
# print(text.endswith("Python"))
# print(text.endswith("python"))

# print("12345".isdigit())
# print("123ab4".isdigit())
# print(",".isdigit())

# print("abcd".isalpha())
# print("1234".isalpha())
# print("123ab4".isalpha())

# print("123".isnumeric())
# print("abc".isnumeric())
# print("123ab4".isnumeric())

# print("123abc".isalnum())
# print("abc".isalnum())
# print("123ab4".isalnum())
# print("England 1920".isalnum())

# print(" ".isspace())
# print("\t".isspace())
# print("123".isspace())
# print("abc".isspace())

# text="Hello, Sanzida"
# print(text.swapcase())

# text2="pYthOn"
# print(text2.swapcase())

# text="hellow"
# print(text.center(20))
# text2="Sanzida"
# print(text2.center(20, "*"))
# print(text2.center(40, "-"))

# text= "hellow"
# print(text.ljust(20))
# print(text.rjust(20, "-"))

# print(text.ljust(20, "*"))
# print(text.rjust(20, "*"))

# name="Sajeeb"
# age=25
# print("My name is {} and I am {} years old".format(name, age))
# print("{0} is {1} years old".format(name, age))
# print(f"My name is {name} and I am {age} years old")

#email validations
# email="martinsajeeb2001@gmail.com"
# if "@" in email and "." in email and email.index("@") < email.index("."):
#     print("Valid Email")
# else:
#     print("Invalid Email")

# password validations
# password=input("Enter your password: ")
# if (len(password)) <= 8:
#     print("Password must be at least 8 characters")
# elif not any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter")
# elif not any(char.islower() for char in password):
#     print("Password must contain at least one lowercase letter")
# elif not any(char.isdigit() for char in password):
#     print("Password must contain at least one digit")
# else:
#     print("Password is valid"

# text="hi monnni ,       ami tomake_ valobasi "
# print(text.strip())
# clean_text=text.strip().replace("_", " ").title()
# clean= " ".join(clean_text.split())
# print(clean)

# csv_line="Sajeeb, 25, Data Analyst, male"
# data=csv_line.title().split(",")
# name=data[0]
# age=data[1]
# job=data[2]
# gender=data[3]
# print(name)
# print(age)
# print(job)
# print(gender)
# print(f"I'm {name}. I'm {age} years old. I'm a {job} myself  {gender}.") 

# Username Validations
# username=input("Enter your username: ")
# if len(username) >= 5:
#     if len(username) <=20:
#         if username[0].isalpha():
#             if username[0].isupper():
#                 if username.isalnum():
#                     print("Username is valid")
#                     print("Your account has been created successfully")
#                 else:
#                     print(" Error: Username must contain only letters and numbers")
#             else:
#                 print("Error: Username must start with a capital letter")
#         else:
#             print("Error: Username must start with a letter")
#     else:       
#         print(" Error: Username must be between 5 and 20 characters")
# else:
#     print(" Error: Username must be at least 5 characters")

#Practice Task
#Write a program that takes user input and:
# raw_text=input("Enter your text: ")
# text=raw_text.split()
# clean_text=" ".join(text)
# print(clean_text)
# vowels="aeiouAEIOU"
# v_count=0
# c_count=0
# for char in clean_text:
#     if char.isalpha():
#         if char in vowels:
#            v_count +=1
#         else:
#             c_count +=1
# print(f"Vowels: {v_count}")
# print(f"Consonants: {c_count}")

#Write a program that validates and extracts email information:
# email=input("Enter your email: ").strip().lower()
# if "@" in email and "." in email:
#     if email.find("@") < email.find("."):
#         parts=email.split("@")
#         username=parts[0]
#         domain=parts[1]
#         print(f"Username: {username}")
#         print(f"Domain: {domain}")
#     else:
#         print("Invalid email format")
# else:
#     print("Invalid email format")

#Write a program that checks password strength:

# import string

# password=input("Enter your password: ").strip()
# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)
# has_digit = any(char.isdigit() for char in password)
# has_special = any(char not in string.ascii_letters + string.digits for char in password)

# criteria_count = sum([has_upper, has_lower, has_digit, has_special])

# if len(password) >= 8:
#     if criteria_count >= 4:
#         print("Password is strong")
#     elif criteria_count >= 2:
#         print("Password is normal")
#     else:
#         print("Password is weak")
# else:
#     print("Password is weak")

#Write a program that takes a URL and extracts:
# url=input("Enter your url (e.g., https://www.google.com): ").strip().lower()
# if "://" in url:
#     protocol_parts= url.split("://")
#     protocol= protocol_parts[0]
#     domain= protocol_parts[1]
#     domain_full= domain.split("/")[0]
#     if "." in domain_full:
#         extensions=domain_full.split(".") [-1]
#         domain_name= domain_full.replace(f".{extensions}", "")
#         print(f"Protocol: {protocol}")
#         print(f"Domain: {domain_name}")
#         print(f"Extension: {extensions}")
#     else:
#         print("Invalid URL format")
# else:
#     print("Invalid URL format")

#Write a program that analyzes text:
# text="Python is a programming language that lets you work quickly and integrate systems more effectively."
# words=text.split()
# word_count=len(words)
# char_count=len(text)
# vowels="aeiouAEIOU"
# v_count=0
# c_count=0
# longest_word=""
# for word in words:
#     if words:
#         longest_word=words[0]
#         for word in words:
#             clean_word=word.strip(".,!")
#             if len(clean_word) > len(longest_word):
#                 longest_word=clean_word
#     for char in word:
#         if char in vowels:
#             v_count +=1
#         else:
#             c_count +=1
# print(f"Word count: {word_count}")
# print(f"Character count: {char_count}")
# print(f"Vowel count: {v_count}")
# print(f"Consonant count: {c_count}")
# print(f"Longest word: {longest_word}") 

# import sys
# security_code=int(input("Enter the security code: "))
# department=input("Enter your department: ").title()
# while True:
#     acess_level=int(input("Enter your access level: "))
#     if acess_level <= 10:
#         break
#     else:
#         print("Invalid access level")
#         continue
# if security_code !=5566:
#     print("Invalid Security code:You won't tget the permissions")
# elif department != "Finance":
#     print("Invalid department:You won't tget the permissions")
# elif acess_level > 10:
#     print("Invalid access level:You won't tget the permissions")
# else:
#     print("Access granted")

# Create Program for online exam system

import sys
regis_num=int(input("Enter your registration number: "))
if regis_num != 192021:
    print("Error: Invalid registration number")
    sys.exit()
subject_name="Python".lower()
subject_name=input("Enter subject name: ").lower()
if subject_name!="python":
  
    print("Error: Invalid subject name:")
    sys.exit()
password=int(input("Enter your password: "))
if password != 9820:
    password=input("Enter your password: ")

password = input("Enter your password: ")
if password != "9820":
    print("Error: Invalid password")
    sys.exit()
print("Access granted")

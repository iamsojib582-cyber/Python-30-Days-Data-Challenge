# phone_numbers={
#     "Sajeeb": "01712345678",
#     "Rahim": "01798765432",
#     "Karim": "01755555555"
# }
# print(f"Sajeeb's phone number: {phone_numbers['Sajeeb']}")
# print(f"Rahim's phone number: {phone_numbers['Rahim']}")
# print(f"Karim's phone number: {phone_numbers['Karim']}")
# print(f"=======================================")

# emp_dict={}
# print(emp_dict)

# person={
#     "name":"Sajeeb",
#     "age":30,
#     "city":"Dhaka"
# }
# person["city"]="Rangpur"
# print(person)
# print(person["name"])
# print(person["age"])
# print(person["city"])

# person=dict(name="Sajeeb", age=30, city="Dhaka")
# print(person)

#accessing values
# sajeeb={
#     "name":"Sajeeb",
#     "age":30,
#     "city":"Dhaka",
#     "date_of_birth": "1993-01-01"
# }
# print(sajeeb["name"])
# print(sajeeb.get("age"))
# print(sajeeb.get("country", "Not Found"))
# print(sajeeb.get("place","N/A"))

#ADing changing values 
# Sajeeb={
#    "sur_name": "Martin",
#    "marital_status": "Married",
#    "hobbies": ["Reading", "Traveling", "Cooking"]

# }
# Sajeeb["age"]=30
# # Sajeeb["city"]="Dhaka"
# # Sajeeb["email"]="sajeeb@example.com"
# # print(Sajeeb)
# Sajeeb["age"]=25
# print(Sajeeb["age"])

# country={
#     "name":"UK", "capital":"London", "population":67_000_000, "currency":"GBP"
# } 
# country.update({
#     "language":"English",
#     "rank":5
#     })
# del country["rank"]

# currency=country.pop("currency")
# print(currency)

# net_worth=country.pop("net_worth","Not Found")
# print(net_worth)

# country.clear()
# print(country)

# employee={
#     "name":"Sajeeb",
#     "age":30,
#     "department":"IT",
#     "hourly_rate":25
# }
# if "name" in employee:
#     print("Name Exists in the dictionary")
# if "age" in employee:
#     print("Age Exists in the dictionary")
# if "salary" in employee:
#     print("Salary Exists in the dictionary")
# else:
#     print("Salary does not exist in the dictionary")

# Loop through dictionary
employee={
    "name":"Sajeeb",
    "age":30,
    "department":"IT",
    "hourly_rate":25
}
# for key in employee:
#     print(f"{key}: {employee[key]}")
# for value in employee.values():
#     print(value)

# for key, value in employee .items():
#      print(f"{key}: {value}")

sajeeb = {"name": "Sajeeb", "age": 21, "city": "Rangpur"}
# keys=sajeeb.keys()
# values=sajeeb.values()
# print(keys)
# print(values)
# keys_list=list(keys)
# values_list=list(values)
# print(keys_list)
# print(values_list)
# values=sajeeb.values()
# print(values)
# values_list=list(values)
# print(values_list)
# items=sajeeb.items()
# print(items)
# items_list=list(items)

# items = sajeeb.items()
# print(items)

# print(len(sajeeb)) 

# sajeeb = {"name": "Sajeeb", "age": 21}
# sajeeb_copy = sajeeb.copy()
# sajeeb_copy["city"] = "Dhaka"
# print(sajeeb)
# print(sajeeb_copy)

# Nested dictionary
employees={
    "emp1":{
       "name": "Sajeeb", 
       "age": 30, 
       "department": "IT",
       "city": "Rangpur"
    },
    "emp2": {
       "name": "Rahim", 
       "age": 28, 
       "department": "HR",
       "city": "Dhaka"
    },
    "emp3": {
       "name": "Karim", 
       "age": 35, 
       "department": "Finance",
       "city": "Chittagong"
    }
}
# print(employees["emp1"]["name"])
# print(employees["emp2"]["age"])
# print(employees["emp3"]["department"])
# print(employees)

# for emp_id, emp_info in employees.items():
#     print(f"{emp_id}: {emp_info['name']} - {emp_info['age']}")

# employees["emp1"]["city"]="Cumilla"
# print(employees["emp1"]["city"])

# employees["emp1"]["Salary"]=50000
# print(employees["emp1"])

# student = {
#     "name": "Sajeeb",           
#     "age": 21,                  
#     "is_active": True,          
#     "subjects": ["Math", "Physics", "Chemistry"],  
#     "grades": {"Math": "A", "Physics": "B"}  
# }
# print(student)
# print(student["name"])
# print(student["age"])
# print(student["is_active"])
# print(student["subjects"][0])
# print(student["grades"]["Math"])

# Customer Data
# customer = {
#     "customer_id": "C001",
#     "name": "Sajeeb",
#     "email": "lFg9k@example.com",
#     "phone": "01712345678",
#     "address": {
#         "street": "123 Main St",
#         "city": "Rangpur",
#         "state": "Rangpur",
#         "zip_code": "5400"
#     },
#     "orders": [
#         {"order_id": "O001", "product": "Laptop", "quantity": 1, "price": 1000},
#         {"order_id": "O002", "product": "Mouse", "quantity": 2, "price": 25}
#     ],
#     "is_active": True
# }
# print(customer)
# print(30*"-")
# print(customer["customer_id"])
# print(customer["name"])
# print(customer["email"])
# print(customer["phone"])
# print(customer["address"]["street"])
# print(customer["address"]["city"])
# print(customer["address"]["state"])
# print(customer["address"]["zip_code"])
# print(customer["orders"][0]["order_id"])
# print(customer["orders"][0]["product"])
# print(customer["orders"][0]["quantity"])
# print(customer["orders"][0]["price"])
# print(customer["is_active"])

# Sales data
# sales_data = {
#    "2024": {
#       "Q1": {
#          "January": {"Sales": 500000, "Expenses": 300000, "Profit": 200000},
#          "February": {"Sales": 600000, "Expenses": 400000, "Profit": 200000},
#          "March": {"Sales": 700000, "Expenses": 500000, "Profit": 200000}
#       },
#       "Q2": {
#          "April": {"Sales": 800000, "Expenses": 600000, "Profit": 200000},
#          "May": {"Sales": 900000, "Expenses": 700000, "Profit": 200000},
#          "June": {"Sales": 1000000, "Expenses": 800000, "Profit": 200000}
#       }
#    },
#    "2023": {
#       "Q1": {
#          "January": {"Sales": 400000, "Expenses": 250000, "Profit": 150000},
#          "February": {"Sales": 450000, "Expenses": 300000, "Profit": 150000},
#          "March": {"Sales": 500000, "Expenses": 350000, "Profit": 150000}
#       }
#    }
# }
# print(sales_data["2023"]["Q1"]["February"]["Sales"])
# print(sales_data["2023"]["Q1"]["February"]["Expenses"])
# print(sales_data["2023"]["Q1"]["February"]["Profit"])
# print(sales_data["2024"]["Q2"]["June"]["Sales"])
# print(sales_data["2024"]["Q2"]["June"]["Expenses"])
# print(sales_data["2024"]["Q2"]["June"]["Profit"])
# print(sales_data["2024"]["Q1"]["March"]["Sales"])
# print(sales_data["2024"]["Q1"]["March"]["Expenses"])
# print(sales_data["2024"]["Q1"]["March"]["Profit"])

#convert list to dictionary
# customer_list=[
#     ["C001", "Ali", "ali@email.com"],
#     ["C002", "Sara", "sara@email.com"],
#     ["C003", "Bob", "bob@email.com"]
# ]
# customers={}
# for customer in customer_list:
#     customers[customer[0]] = {
#         "name": customer[1],
#         "email": customer[2]
#     }
# print(customers)

# import pandas as pd
# customers_df = pd.DataFrame([
#     {"id": "C001", "name": "Ali", "age": 30},
#     {"id": "C002", "name": "Sara", "age": 28},
#     {"id": "C003", "name": "Bob", "age": 32}
# ])
# print(customers_df)

sales_record = {
    "transaction_id": "TRX001",
    "date": "2024-03-11",
    "customer_name": "Ali Khan",
    "product": "Laptop",
    "quantity": 2,
    "price_per_unit": 50000,
    "total_amount": 100000,
    "discount_percent": 10,
    "final_amount": 90000,
    "status": "Completed"
}

# print(sales_record["final_amount"])
# if sales_record["discount_percent"] > 0:
#     print(f"Discount Applied: {sales_record['discount_percent']}%")
# else:
#     print("No discount applied.")

# for key, value in sales_record.items():
#     print(f"{key}: {value}")

sales_record["payment_method"] = "Credit Card"
print(sales_record)
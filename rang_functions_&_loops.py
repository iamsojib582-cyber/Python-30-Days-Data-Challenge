# for i in range(5):
#     print(f"Iteration {i}")

# for i in range(1, 11):
#     print(f"{i} squared is {i**2}")

# for i in range(2,7):
#     print(i)

# for i in range(0, 10, 2):
#     print(f"Even number: {i}")

# for i in range(1,11,2):
#     print(f"Odd number: {i}")

# for i in range (10, 0, -1):
#     print(f"Countdown: {i}")

# for i in range (5):
#     print(f"Iteration {i}")

# customer=["Ali", "Sara", "Bob"]
# for customers in customer:
#     print(f"Customer: {customers}")

# customer=["monni", "sara", "bob"]
# for i in range(len(customer)):
#     print(f"Customer {i}: {customer[i]}")

# sudent={"name":"Sajeeb", "age": 22, "major": "Computer Science"}
# for key in sudent:
#     print(f"{key}: {sudent[key]}")

# for key, value in sudent.items():
#     print(f"{key}: {value}")

# customers_id={
#     "C001": {"name": "Ali", "email": "ali@email.com"},
#     "C002": {"name": "Sara", "email": "sara@email.com"},
#     "C003": {"name": "Bob", "email": "bob@email.com"}
# }
# for customer_id, customer_info in customers_id.items():
#     print(f"Customer ID: {customer_id}")
#     for key, value in customer_info.items():
#         print(f"{key}: {value}")
    
# unique_customers={"Ali", "Sara", "Bob", "Ali", "Sara"}
# for customer in unique_customers:
#     print(f"Unique Customer: {customer}")

# count=0
# while count <= 5:
#     print(f"Count: {count}")
#     count += 1

# age=int(input("Enter your age: "))
# while age < 18:
#     print(f"Age:{age} is less than 18. Please enter a valid age.")
#     age+=1
# print(f"Age: {age} is valid. You can proceed.")

# count=int(input("Enter a number: "))
# while count <10:
#     if count == 5:
#         break
#     print(f"Count: {count}")
#     count += 1
# print("Loop ended.")

# count=0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(f"Count: {count}")

# count=0
# for i in range(21):
#     if i in (5, 10, 15, 20):
#         continue
#     print(i)

# count=0
# while count < 10:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(f"Odd Count: {count}")

# count=0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(f"Count: {count}")

# customers=["Ali", "Sara", "Bob", "Monni", "Sajeeb"]
# purchages=[1000, 2000, 1500, 3000, 2500]
# print("Customer Sales Report:")
# for i in range(len(customers)):
#     print(f"{customers[i]}: ${purchages[i]}")

# sales=[1000, 2000, 1500, 3000, 2500]
# total=0
# for sale in sales:
#     total += sale
# print(f"Total Sales: ${total}")

#Filter Data
# sales=[20000, 5000, 15000, 8000, 12000]
# high_sales=[]
# for sale in sales:
#     if sale > 10000:
#         high_sales.append(sale)
# print(f"High Sales: {high_sales}")

# customer_ids=["M2001", "M2001", "M2002", "M2003", "M2002"]
# for customer in set (customer_ids):
#     count=customer_ids.count(customer)
#     print(f"Customer ID: {customer}, Count: {count}")

# discouts prices
# Product_name=["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"]
# price=[1000, 500, 300, 150, 200]
# discounted_prices=[]
# for i in range(len(Product_name)):
#     discounted_price=price[i]*0.9
#     discounted_prices.append(discounted_price)
#     print(f"{Product_name[i]}: Original Price: ${price[i]}, Discounted Price: ${discounted_price:.2f}")

month=["January", "February", "March", "April", "May"]
# sales=[10000, 15000, 12000, 18000, 20000]
# for i in range(len(month)):
#   month=month[i]
#   amount=sales[i]
#   if amount > 15000:
#     status="Exellent"
#   elif amount > 12000:
#     status="Good"
#   else:    status="Average"
#   print(f"{month}: Sales: ${amount}, Status: {status}")

# months = ["January", "February", "March"]
# sales = [100000, 150000, 120000]

# for i in range(len(months)):
#     month = months[i]
#     amount = sales[i]
    
#     if amount > 125000:
#         status = "Excellent"
#     elif amount > 100000:
#         status = "Good"
#     else:
#         status = "Average"
    
#     print(f"{month}: ${amount} ({status})")

# customer_ids=["C001", "C002", "C003", "C004", "C005"]
# customer_names=["Ali", "Sara", "Bob", "Monni", "Sajeeb"]
# purchases=[1000, 2000, 1500, 3000, 2500]
# customers={}
# for i in range(len(customer_ids)):
#     customer_id=customer_ids[i]
#     name=customer_names[i]
#     purchase=purchases[i]
#     customers[customer_id] = {
#         "name": name,
#         "purchase": purchase
#     }
# print(customers)

#Data Validatioin 
# emails=[
#     "sajeeb@gmailcom",
#     "rifaemail.com",
#     "sanjida@hmaolcom",
#     "monni@gmailcom",
#     "sara@gmailcom",
#     "martin@hmail.com"
# ]
# print("Email Validation Report:")
# for email in emails:
#     if "@" in email and email.endswith(".com"):
#         print(f"Valid Email: {email}")
#     else:
#         print(f"Invalid Email: {email}")

# for i in range(5,9):
#     for j in range(3,8):
#         result=i*j
#         print(f"{i} x {j} = {result}")
#     print("-"*30)

# stores={
#     "store1":{"revenue":500000, "customers": 2000},
#     "store2":{"revenue":750000, "customers": 3000},
#     "store3":{"revenue":600000, "customers": 2500}
# }
# # for store_name,data in stores.items():
# #     revenue=data["revenue"]
# #     customers=data["customers"]
# #     print(f"{store_name}: Revenue: ${revenue}, Customers: {customers}")

# for store_name, data in stores.items():
#     print(f"\n{store_name}:")
#     for key, value in data.items():
#         print(f"  {key}: {value}")

# customers=["Ali", "Sara", "Bob", "Monni", "Sajeeb"]
# for index, customer in enumerate(customers):
#     print(f"Customer {index+1}: {customer}")

# products = ["Laptop", "Phone", "Tablet"]
# prices = [50000, 30000, 20000]
# for index, product in enumerate(products):
#     price=prices[index]
#     print(f"{product}: ${price}")

# name=["Ali", "Sara", "Bob", "Monni", "Sajeeb"]
# ages=[20, 25, 30, 35, 40]
# cities=["New York", "London", "Paris", "Tokyo", "Sydney"]
# for name, age, city in zip(name, ages, cities):
#    print(f"{name} is {age} years old and lives in {city}")
#    print("Ended")

# customer_id=["C001", "C002", "C003", "C004", "C005"]
# customer_name=["Ali", "Sara", "Bob", "Monni", "Sajeeb"]
# purchages=[1000, 2000, 1500, 3000, 2500]
# for oid, name, amount in zip(customer_id, customer_name, purchages):
#     print(f"{oid} - {name}: ${amount}")

# for i in range(10):
#     if i == 7:
#         break
#     print(i)

# for i in range(10):
#     if i == 7:
#         continue
#     print(i)

# for i in range(5):
#     if i == 8:
#         break
#     print(i)
# else:
#     print("Loop completed successfully.")

# customers=["C001", "C002", "C003", "C004", "C005"]
# for customer in customers:
#     print(customer)

# password_attempts=0
# while password_attempts < 3:
#     password=input("Enter your password: ")
#     if password == "password":
#         print("Access granted.")
#         break
#     else:
#         print("Incorrect password. Please try again.")
#         password_attempts += 1

sales_data = [
    {"customer": "C001", "amount": 5000},
    {"customer": "C002", "amount": 7500},
    {"customer": "C001", "amount": 3200},
    {"customer": "C003", "amount": 9000},
    {"customer": "C002", "amount": 4500}
]

# customer_totals = {}
# for sale in sales_data:
#     customer = sale["customer"]
#     amount = sale["amount"]
#     if customer in customer_totals:
#         customer_totals[customer] += amount
#     else:
#         customer_totals[customer] = amount

# for customer, total in customer_totals.items():
#     print(f"Customer {customer}: ${total}")

 
products = ["Laptop", "Phone", "Tablet", "Monitor"]
prices = [50000, 30000, 20000, 15000]
quantities = [10, 25, 15, 30]
# # for product, price in zip(products, prices):
# #     print(f"{product}: ${price}")
# # print("-"*30)
# # for products,prices,quantities in zip(products,prices,quantities):
# #     print(f"{products}: ${prices} x {quantities} = ${prices*quantities}")

# for quantity in quantities:
#     if quantity > 20:
#         print("Quantity is more than 10")
#     else:
#         print("Quantity is less than or equal to 10")

average_price = sum(prices) / len(prices)
print(f"Average price: ${average_price:.2f}")


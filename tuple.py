# # list_data=[10,20,30,40,50]
# # list_data[0]=100
# # print(list_data)

# # tuple_data=(10,20,30,40,50)
# # tuple_data[0]=100
# # print(tuple_data

# # numbers=(10,20,30,40,50)
# # print(numbers[0])
# # print(numbers[1])
# # print(numbers[2])
# # print(numbers[3])
# # print(numbers[4])

# # for num in numbers:
# #     print(num)
# # for i in range(len(numbers)):
# #     print(f"{i}: {numbers[i]}")

# # for i, num in enumerate(numbers):
# #     print(f"{i}: {num}")

# # single = (1,)
# # print(type(single))
# # sinle2=(1)
# # print(type(sinle2))
# # numbers=1,11,22
# # print(type(numbers))

# # mixed=(10, "Hello", 3.14, [1, 2, 3], (4, 5))
# # print(mixed)

# # empty=()
# # print(type(empty))

# # my_list = [1, 2, 3]
# # my_tuple = tuple(my_list)
# # print(my_tuple)

# # data = ("John", 25, 50000, "Engineer")
# # print(data[0])
# # print(data[1])
# # print(data[2])
# # print(data[-1])
# # print(data[0:2])
# # print(data[1:])

# # employee=("John", 25, 50000, "Engineer")
# # name, age, salary, profession = employee
# # print(f"Name: {name}")
# # print(f"Age: {age}")
# # print(f"Salary: {salary}")
# # print(f"Profession: {profession}")

# # price, quantity = (9345672, 5)
# # total_cost = price * quantity
# # print(f"Total Cost: {total_cost}")

# # a = 5
# # b = 10
# # a,b=b,a
# # print(f"a: {a}, b: {b}")

# # numbers = (1, 2, 2, 3, 2, 4)
# # print(numbers.count(2))

# # colours=("red", "green", "blue", "green", "yellow")
# # print(colours.count("green"))

# # fruits = ("apple", "banana", "orange")
# # print(fruits.index("banana"))

# # numbers = (10, 20, 30, 40, 50)
# # print(numbers.index(30))

# # transaction_list = [2025, 2, 25, 5000, "Completed"]
# # transaction_list[0] = 2024
# # print(transaction_list)

# # details=(2025, 2, 25, 5000, "Completed")
# # details[0]=2024
# # print(details)

# # stock_data = {
# #     ("AAPL", 2025, 1): 150.00,
# #     ("AAPL", 2025, 2): 155.00,
# #     ("MSFT", 2025, 1): 380.00,
# # }
# # print(stock_data[("AAPL", 2025, 1)])

# # stoct_details={
# #     ["AAPL", 2025, 1]: 150.00,
# #     ["AAPL", 2025, 2]: 155.00,
# #     ["MSFT", 2025, 1]: 380.00,

# # } 
# # print(stoct_details[["AAPL", 2025, 1]])

# # def analyze_sales(sales_data):
# #     total = sum(sales_data)
# #     average = total / len(sales_data)
# #     highest = max(sales_data)
# #     lowest = min(sales_data)
# #     return total, average, highest, lowest
# # sales = [100, 200, 150, 300, 250]
# # total, avg, max_val, min_val = analyze_sales(sales)
# # print(f"Total Sales: {total}")
# # print(f"Average Sales: {avg}")
# # print(f"Highest Sale: {max_val}")
# # print(f"Lowest Sale: {min_val}")

# # import sys
# # my_list = [1, 2, 3, 4, 5]
# # my_tuple = (1, 2, 3, 4, 5)
# # print(f"List: {my_list}, Size: {sys.getsizeof(my_list)} bytes")
# # print(f"Tuple: {my_tuple}, Size: {sys.getsizeof(my_tuple)} bytes")

# # employees = (("John", 50000), ("Alice", 60000), ("Bob", 55000))
# # for emp in employees:
# #     print(emp)
# # for name, salary in employees:
# #     print(f"Name: {name}, Salary: {salary}")
# # for i, (name, salary) in enumerate(employees):
# #     print(f"{i}: Name: {name}, Salary: {salary}")

# # Tuoles vs List Comparison
# # my_list = [1, 2, 3, 4, 5]
# # my_list[0] = 100
# # my_list.append(6)

# # my_tuple = (1, 2, 3, 4, 5)
# # my_tuple = list(my_tuple)
# # my_tuple[0] = 100
# # my_tuple.append(6)
# # my_tuple = tuple(my_tuple)

# # customer = ("John Smith", 25, "john@email.com", "Active")
# # name,age,gmail,status=customer
# # print(f"Name: {name}")
# # print(f"Age: {age}")
# # print(f"Gmail: {gmail}")
# # print(f"Status: {status}")

# def analyze_dataset(data):
#     return (
#         sum(data),
#         len(data),
#         max(data),
#         min(data),
#         sum(data) / len(data) if len(data) > 0 else 0
#     )
# sales= [100, 200, 150, 300, 250]
# total, count, highest, lowest, average = analyze_dataset(sales)
# print(f"Sales Analysis:")
# print(f"Total Sales: {total}")
# print(f"Number of Sales: {count}")
# print(f"Highest Sale: {highest}")
# print(f"Lowest Sale: {lowest}")
# print(f"Average Sale: {average}") 

# sales_data = {
#     ("2025-01", "North"): 50000,
#     ("2025-01", "South"): 45000,
#     ("2025-02", "North"): 55000,
#     ("2025-02", "South"): 48000,
# }
# jan_north_sales = sales_data[("2025-01", "North")]
# print(f"January North Sales: {jan_north_sales}")
# for (month, region), sales in sales_data.items():
#     print(f"{month} - {region}: ${sales}")

# location={
#     (40.7128, -74.0060), "Los Angeles":,
#     (34.0522, -118.2437),"Chicago":,
#     (51.5074, -0.1278),"London":
# }
# for lat, lon in location:
#     print(f"Latitude: {lat}, Longitude: {lon}")

# valid_employee = ("E001", "John", "IT", 50000)
# def print_employee(emp_tuple):
#     emp_id, name, department, salary = emp_tuple
#     print(f"Employee ID: {emp_id}")
#     print(f"Name: {name}")
#     print(f"Department: {department}")
#     print(f"Salary: ${salary}")


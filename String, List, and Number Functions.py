# text="My name is Sajeeb"
# print(len(text))

# text2="hey I'm Sajeeb"
# print(text2.split(",")) 

# name="sajeeb, sanzida"
# print(name.upper())

# name="sajeeb, sanzida"
# print(name.title())

# text="HELLOW"
# print(text.lower())

# text2="my name is sajeeb and i'm from bangladesh"
# print(text2.capitalize())

# text3="I love python"
# text4=text3.replace("python", "java")
# print(text4.title())

# text5="Sajeeb, Nami, Sanzida, Sathi, Monni"
# text6=text5.split(",")
# print(text6)

# text7="monni, sathi, sanzida"
# result=", ".join(text7)
# print(result)

# text8="         hellow        "
# print(text8.strip())
# print(text8.lstrip())
# print(text8.rstrip())

# text10="helllow, world"
# print(text10.startswith("hello"))
# print(text10.endswith("world"))
# print(text10.find("world"))
# print("world" in text10)

# text="apple, banana, juice, apple"
# print(text.count("apple"))

# tex2="hello123"
# print(tex2.isalpha())
# print(tex2.isnumeric())
# print(tex2.isalnum())
# print(tex2.isspace())

# print("12345".isdigit())
# print("123abc".isdigit())

email="iamsojib582@gmail.com"
# print(email.split("@")[1].split(".")[0])
# if email.find("@") < email.find("."):
#     print("Username: " + email.split("@")[0])
#     print("Domain: " + email.split("@")[1].split(".")[0])
# else:
#     print("Invalid email format")

# if "@" in email and "." in email:
#     if email.find("@") < email.find("."):
#         print("Valid Email")
#     else:
#         print("Invalid email format")

# customer_names=["sajeeb", "sanzida", "sathi", "monni"]
# customer_names.sort()
# print(customer_names)

# formatted_names=[name.title() for name in customer_names]
# print(formatted_names)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# squares=[num**2 for num in numbers]
# print(squares)

# numbers=[2,3,4,5,6]
# print(len(numbers))

# fruits=["apple", "banana", "cherry"]
# # fruits.append("orange")
# # print(fruits)
# fruits.extend(["mango", "pineapple"])
# print(fruits)

# fruits=["apple", "banana", "cherry"]
# fruits.insert(1, "orange")
# print(fruits)

# fruits2=["apple", "banana", "cherry"]
# fruits2.remove("apple")
# print(fruits2)

# fruits3=["apple", "banana", "cherry"]
# fruits3.pop(1)
# print(fruits3)

# fruits4=["apple", "banana", "cherry"]
# position=fruits4.index("cherry")
# print(position)

# numbers=[1,2,3,4,5,5]
# count=numbers.count(5)
# print(count)

# numbers2=[3,4,5,2,9]
# numbers2.sort()
# print(numbers2)

# numbers3=[3,4,5,2,9]
# numbers3.sort(reverse=True)
# print(numbers3)

# numbers4=[3,4,5,2,9]
# numbers4.reverse()
# print(numbers4)

# numbers5=[3,4,5,2,9]
# numbers5.clear()
# print(numbers5)

# original=[1,2,3,4,5]
# copy=original.copy()
# copy.append(6)
# print(copy)
# print(original)

# sales=[5000000, 7000000, 900000, 100000000000,888700, 800000]
# highest=max(sales)
# lowest=min(sales)
# highest=max(sales)
# total=sum(sales)
# average=total/len(sales)
# print(f"Highest Sales: ${highest}")
# print(f"Lowest Sales: ${lowest}")
# print(f"Total Sales: ${total}")
# print(f"Average Sales: ${average}") 

# customer_ids=["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
# unique=list(set(customer_ids))
# unique.sort()
# print(len(customer_ids))
# print(unique)

# print(abs(-5))
# print(round(3.14159, 2))

numbers=[5,6,6,7,8,9,10]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sum(numbers) / len(numbers))

# price=19.99
# tax=0.07
# total_price= price + (price * tax)
# print("Total price is: ", total_price)

# print(f"{price:.2f}")

# total=9460.872
# print(round(total,2))
# print(f"${total:.2f}")

# percentage= 0.85
# print(f"{percentage:.1%}")

# big_number=1000000
# print(f"{big_number:,}")

# print(pow(2,3))
# print(pow(2,3,9))

# import math 
# print(math.sqrt(16))

# print(int(4.99))
# print(float(4))
# print(str(4.99))
# print(bool(1))
# print(bool(0))

# print(isinstance(5, int))

# print(isinstance(5.5, float))

# print(isinstance(5.5, float))

# sales=[50000,75000,32000,90000]
# highest=max(sales)
# lowest=min(sales)
# total=sum(sales)
# average=total/len(sales)
# print(f"Highest Sales: ${highest}")
# print(f"Lowest Sales: ${lowest}")
# print(f"Total Sales: ${total}")
# print(f"Average Sales: ${average}")

# prices=[100, 200, 300, 400, 500]
# discount_percent=0.20
# discounted = [round(price * (1 - discount_percent/100), 2) for price in prices]
# print(discounted)

# customers="Ali Khan, Sara Ahmed, Bob Smith"
# customer_names=customers.split(", ")
# print(customer_names)

# prices=[1000,2000,1500,890]
# discount_percent=10
# discounted = [round(price * (1 - discount_percent/100), 2) for price in prices]
# print(discounted)

# customers="Ali Khan, Sara Ahmed, Bob Smith"
# customer_names=customers.split(", ")
# customers_names=[name.title() for name in customer_names]
# count=len(customers_names)
# print(f"Numbers of customers: {count}")
# print(f"Customers: {customers_names}")

sales_text="888000,98000,556600,230000,89000"
# sales=[int(sale) for sale in sales_text.split(",")]
# total=sum(sales)
# average=total/len(sales)
# highet=max(sales)
# lowest=min(sales)

# report=f"""
# Sales Report
# Total Sales: ${total}
# Average Sales: ${average}
# Highest Sales: ${highet}
# Lowest Sales: ${lowest}
# """
# print(report)

# email_string = "ali@example.com, sara@domain.com, bob@test.com"
# emails=email_string.split(", ")
# emails=[email.strip().lower() for email in emails]
# valid_emails=[email for email in emails if "@" in email and email.endswith(".com")]
# print(f"Total number of emails: {len(emails)}")
# print(f"Valid emails: {len(valid_emails)}")
# print(f"Valid list:{', '.join(valid_emails)}")

# customers_text="Ali Khan, Sara Ahmed, Bob Smith"
# sales_text="5000,5555,89000"
# customer_list=customers_text.split(", ")
# customer_list=[customer.strip().title() for customer in customer_list]
# sales_list=[int(sale) for sale in sales_text.split(",")]
# total_sales=sum(sales_list)
# average_sales=total_sales/len(sales_list)
# hoghest_sales=max(sales_list)
# lowest_sales=min(sales_list)
# report=f"""
# Sales Report
# Total Sales: ${total_sales}
# Average Sales: ${average_sales}
# Highest Sales: ${hoghest_sales}
# Lowest Sales: ${lowest_sales}
# """
# print(report)

# products = "Laptop, Phone, Tablet"
# prices = "50000,30000,20000"
# product_list=products.split(", ")
# product_list = [product.strip().upper() for product in products.split(", ")]
# prices_list=[int(price) for price in prices.split(",")]
# total_price=sum(prices_list)
# average_price=total_price/len(prices_list)
# maximum=max(prices_list)
# minimum=min(prices_list)
# report=f"""
# Sales Report
# Total Sales: ${total_price}
# Average Sales: ${round(average_price, 2)}
# Highest Sales: ${maximum}
# Lowest Sales: ${minimum}
# """
# print(report)

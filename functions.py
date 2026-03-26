# def great ():
#     print("Hello")
#     print("How are you?")
#     print("I am fine")
#     print("Thank you")

# great()

# def great_user (name):
#     print(f"Hello {name}")
#     print("How are you?")
#     print("I am fine")
#     print("Thank you")

# great_user("Sajeeb")
# great_user("Sanzida")
# great_user("Sarmin")

# def add_numners (a,b):
#     return a + b
#     return result
# sum1=add_numners(10,20)
# sumb=add_numners(30,40)
# print(sum1)
# print(sumb)

# def calculate_discount(price, discount_percent):
#     discount_amount = price * (discount_percent / 100)
#     discounted_price = price - discount_amount
#     return discounted_price
# original_price=34
# discount_percentage=10
# discounted=calculate_discount(original_price, discount_percentage)
# print(f"Original Price: ${original_price}")
# print(f"Discount Percentage: {discount_percentage}%")
# print(f"Discount Amount: ${discounted}")

# def calculate_total_sales(quantity, price_per_unit,tax_amount):
#      subtotal= quantity * price_per_unit
#      tax=subtotal * (tax_amount / 100)
#      total=subtotal + tax
#      return total

# total_sales=calculate_total_sales(10,200000,5)
# print(f"Total Sales: ${total_sales}")

# def apply_discount(price, discount_percentage=10):
#     return price * (1 - discount_percentage / 100)

# print(apply_discount(100))
# print(apply_discount(100, 20))

# def get_min_max (numbers):
#     return min(numbers), max(numbers)
# data=[10,20,30,40,50]
# min_value, max_value=get_min_max(data)
# print(f"Minimum value: {min_value}")
# print(f"Maximum value: {max_value}")

# def analyze_sales (sales_list):
#     return{
#         "total": sum(sales_list),
#         "average": sum(sales_list) / len(sales_list),
#         "count": len(sales_list),
#         "max": max(sales_list),
#         "min": min(sales_list)
#     }
# sales = [5000, 7500, 3200, 9000]
# results = analyze_sales(sales)
# print(f"Total: ${results['total']}")
# print(f"Average: ${results['average']}")
# print(f"Count: {results['count']}")

# def remove_duplicates(data_list):
#     return list(set(data_list))
# customer_ids=[101, 102, 103, 104, 101, 102, 105]
# unique_ids=remove_duplicates(customer_ids)
# print(unique_ids)

# def calculate_average(values):
#     if len (values) == 0:
#         return 0
#     return sum(values) / len(values)

# data=[10,20,30,40,50]
# average=calculate_average(data)
# print(f"Average: {average}")

# def filter_high_sales(sales_list, threshold):
#     return [sale for sale in sales_list if sale > threshold]

# sales = [5000, 7500, 3200, 9000]
# filtered_sales = filter_high_sales(sales, 5000)
# print(filtered_sales)

# def is_valid_email(email):
#     return "@" in email and "." in email
# emails=[
#     "sajeeb@gmailcom",
#     "rifaemail.com",
#     "sanjida@hmaolcom",
#     "monni@gmailcom",
#     "sara@gmailcom",
#     "martin@hmail.com"]
# for email in emails:
#     if is_valid_email(email):
#         print(f"Valid Email: {email}")
#     else:
#         print(f"Invalid Email: {email}")

# def apply_bulk_discount(quantity, price):
#     if quantity >100:
#         discount=0.20
#     elif quantity >50:
#         discount=0.10
#     elif quantity >20:
#         discount=0.05
#     else:
#         discount=0
#     total=quantity * price * (1-discount)
#     return total, discount *100
# total1, discount1=apply_bulk_discount(5,100)
# total2, discount2=apply_bulk_discount(50,100)
# total3, discount3=apply_bulk_discount(100,100)
# print(f"Total: ${total1}")
# print(f"Total: ${total2}")
# print(f"Total: ${total3}")

# def customer_process_data(customoer_list):
#     total_customers=len(customoer_list)
#     unique_customers=set(customoer_list)
#     duplicates_count=len(customoer_list)-len(unique_customers)
#     return{
#         "total_customers": total_customers,
#         "unique_customers": unique_customers,
#         "duplicates_count": duplicates_count
#     }
# customers=["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015", "C016", "C017", "C018", "C019", "C020"]
# results=customer_process_data(customers)
# print(f"Total Customers: {results['total_customers']}")
# print(f"Unique Customers: {results['unique_customers']}")
# print(f"Duplicate Customers: {results['duplicates_count']}")

# def format_currency(amount, currency_symbol="$"):
#     return f"{currency_symbol}{amount:.2f}"
# sales=[5000, 7500, 3200, 9000]
# for sale in sales:
#     formatted_amount=format_currency(sale)
#     print(f"Sales: {formatted_amount}")

# def calculate_tax(amount, tax_rate=0.14):
#     tax=amount*tax_rate
#     total=amount+tax
#     return {
#         "subtotal": amount,
#         "tax": tax,
#         "total": total
#     }
# result=calculate_tax(1000)
# print(f"Subtotal: {result['subtotal']}")
# print(f"Tax: {result['tax']}")
# print(f"Total: {result['total']}")

# def sum_sales(sales_list):
#     total=0
#     for sale in sales_list:
#         total+=sale
#     return total
# sales=[5000, 7500, 3200, 9000]
# total_sales=sum_sales(sales)
# print(f"Total Sales: ${total_sales}")

# def calculate_averages(data_dict):
#     average={}
#     for category, values in data_dict.items():
#         average[category]=sum(values)/len(values)
#         average[category]=round(average[category],2)
#     return average
# sales_by_quarter={
#     "Q1": [100, 200, 300],
#     "Q2": [400, 500, 600],
#     "Q3": [700, 800, 900],
#     "Q4": [1000, 1100, 1200]
# }
# averages=calculate_averages(sales_by_quarter)
# print(averages)

# def build_customer_dict(ids,names,emails):
#     customer_dict={}
#     for i in range (len(ids)):
#         customer_dict[ids[i]]={"name":names[i], "email":emails[i]}
#     return customer_dict
# ids=["C001", "C002", "C003", "C004", "C005"]
# names=["Sajeeb", "Rifa", "Sanjida", "Monni", "Sara"]
# emails=["sajeeb@gmailcom", "rifaemail.com", "sanjida@hmaolcom", "monni@gmailcom", "sara@gmailcom"]
# customer_dict=build_customer_dict(ids,names,emails)
# print(customer_dict)

# def grade_sales(amount):
#     if amount > 1000000:
#         return "Exellent"
#     elif amount > 500000:
#         return "Good"
#     elif amount > 300000:
#         return "Average"
#     else:
#         return "Bad"
# sales=[120000, 800000, 600000, 400000]
# for sale in sales:
#     grade=grade_sales(sale)
#     print(f"Sales: ${sale}, Grade: {grade}")

# def categorize_customers(purchage_amount):
#     if purchage_amount > 100:
#         print("Gold")
#     elif purchage_amount > 50:
#         print("Silver")
#     else:
#         print("Bronze")
# customers={
#     "C001": 80,
#     "C002": 40,
#     "C003": 60,
#     "C004": 30,
#     "C005": 90
# }
# for customer, amount in customers.items():
#     category=categorize_customers(amount)
#     print(f"{customer}: {category} (${amount})")

# def calculate_roi (investment,profit):
#     return (profit/investment)*100

# investment=100000
# profit=50000
# roi=calculate_roi(investment,profit)
# print(f"ROI: {roi}%")

# def remove_duplicates(data):
#     unique_data = []
#     seen = set()
#     for item in data:
#         if item not in seen:
#             unique_data.append(item)
#             seen.add(item)
#     return unique_data

# data = [1, 2, 2, 3, 4, 4, 5, 5]
# result = remove_duplicates(data)
# print(result)

# def calculate_average(values):
#     if not values:
#         return 0
#     return sum(values) / len(values)

# values = [1, 2, 3, 4, 5]
# average = calculate_average(values)
# print(f"Average: {average}")

# def filter_high_values (data, threshold):
#     return [value for value in data if value > threshold]

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_data = filter_high_values(data, 7)
# print(filtered_data)
 
# def remove_duplicates(data):
#     unique_data = []
#     seen = set()
#     for item in data:
#         if item not in seen:
#             unique_data.append(item)
#             seen.add(item)
#     return unique_data

# def calculate_average(values):
#     if not values:
#         return 0
#     return sum(values) / len(values)

# def filter_high_values(data, threshold):
#     return [value for value in data if value > threshold]

# def generate_report(data_list):
#     unique=remove_duplicates(data_list)
#     average=calculate_average(data_list)
#     high=filter_high_values(data_list,average)
#     return {
#         "total_items": len(data_list),
#         "unique_items": unique,
#         "average": average,
#         "high_values": high

#     }
# sales=[5000, 7500, 3200, 9000]
# report=generate_report(sales)
# print(report)
# for key, value in report.items():
#     print(f"{key}: {value}")


# def calculate_comission(sales_amount):
#     if sales_amount > 100000:
#         return sales_amount * 0.1
#     elif sales_amount > 50000:
#         return sales_amount * 0.05
#     else:
#         return 0

# sales=[50000, 75000, 32000, 90000]
# for sale in sales:
#     comission=calculate_comission(sale)
#     print(f"Sales: ${sale}, Comission: ${comission}")

# Function to validate customer ID (must be 'C' + 3 digits)
# def is_valid_customer_id(customer_id):
#     return customer_id.startswith("C") and len(customer_id) == 5

# customer_ids = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
# for customer_id in customer_ids:
#     if is_valid_customer_id(customer_id):
#         print(f"Valid customer ID: {customer_id}")
#     else:
#         print(f"Invalid customer ID: {customer_id}")

#Function to categorize sales (Low/Medium/High)
# def categorize_sales(sales_amount):
#     if sales_amount < 50000:
#         return "Low"
#     elif sales_amount < 100000:
#         return "Medium"
#     else:
#         return "High"

# sales=[50000, 75000, 32000, 90000]
# for sale in sales:
#     category=categorize_sales(sale)
#     print(f"Sales: ${sale}, Category: {category}")

#Function to process sales list and return summary
def process_sales(sales_list):
    total_sales = sum(sales_list)
    average_sales = total_sales / len(sales_list)
    high_sales = max(sales_list)
    low_sales = min(sales_list)
    return {
        "total_sales": total_sales,
        "average_sales": average_sales,
        "high_sales": high_sales,
        "low_sales": low_sales
    }

sales = [5000, 7500, 3200, 9000]
results = process_sales(sales)
print(f"Total Sales: ${results['total_sales']}")
print(f"Average Sales: ${results['average_sales']}")
print(f"High Sales: ${results['high_sales']}")
print(f"Low Sales: ${results['low_sales']}")
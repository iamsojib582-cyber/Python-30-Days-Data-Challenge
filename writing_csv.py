# data = [
#     ["Customer_ID", "Name", "Purchase"],
#     ["C001", "Ali Khan", "5000"],
#     ["C002", "Sara Ahmed", "7500"],
#     ["C003", "Bob Smith", "3200"]
# ]
# with open("output.csv", "w") as file:
#     for row in data:
#         line = ",".join(row) + "\n"
#         file.write(line)
# print("File saved successfully!")
       
# data = [
#     "Customer_ID,Name,Purchase\n",
#     "C001,Ali Khan,5000\n",
#     "C002,Sara Ahmed,7500\n",
#     "C003,Bob Smith,3200\n"
# ]
# with open("output.csv", "w") as file:
#     file.writelines(data)
# print("File saved successfully!")

# new_data = "C004,Diana Prince,8000\n"

# with open("output.csv", "a") as file:
#     file.write(new_data)

# print("Data appended!")

# with open("messy_data.csv", "r") as file:
#     lines = file.readlines()
#     header=lines[0]
#     cleaned_data=[header]
#     for line in lines[1:]:
#        cleaned_line = line.strip()
#        if cleaned_line:
#            values=cleaned_line.split(",")
#            values=[v.strip() for v in values]
#            cleaned_data.append(",".join(values) + "\n")
# with open("cleaned_data.csv", "w") as file:
#     file.writelines(cleaned_data)
# print("Data cleaned and saved!")


with open("sales_data.csv", "r") as file:
    lines = file.readlines()
    total_sales = 0
count = 0
cities = set()
max_sale = 0
max_customer = ""
for line in lines[1:]:
    values = line.strip().split(",")
    if len(values) >= 5:
        try:
            amount = float(values[4])
            total_sales += amount
            count += 1
            
            cities.add(values[5])
            
            if amount > max_sale:
                max_sale = amount
                max_customer = values[1]
        except ValueError:
            pass
average = total_sales / count if count > 0 else 0
report = f"""SALES REPORT
SUMMARY METRICS:
Total Sales: ${total_sales:.2f}
Average Sale: ${average:.2f}
Transaction Count: {count}
Cities: {len(cities)}
Highest Sale: ${max_sale:.2f} ({max_customer})
CITIES:
{', '.join(sorted(cities))}
"""
with open("sales_report.txt", "w") as file:
    file.write(report)

print("Report saved to 'sales_report.txt'")
print(report)
print("Report saved to 'sales_report.txt'")
print(report)
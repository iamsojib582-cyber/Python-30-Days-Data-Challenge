# list=[1,22,22,33,44,55]
# set=set(list)
# print(set)

# unique_numbers = {1, 2, 3}
# empty_set= set()
# print(unique_numbers)
# print(empty_set)
# print(type(unique_numbers))
# print(type(empty_set))

# from numpy import sort


# country={"Bangladesh", "India", "Pakistan", "Nepal", "Bhutan"}
# # country.add("Sri Lanka")
# country.update(["Afghanistan", "Maldives"])
# # print(sort(list(country)))
# country.remove("Bangladesh")
# country.discard("Nepal")
# if "India" in country:
#     print("India is in the set")
# print(country)

# set1={1, 2, 3, 4, 5}
# set2={4, 5, 6, 7, 8}
# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # print(set1.difference(set2))
# # print(set2.difference(set1))
# # print(set1.symmetric_difference(set2))

# all_items=set1 | set2
# common_items=set1 & set2
# unique_to_set1=set1 - set2
# unique_to_set2=set2 - set1
# print("All items:", all_items)
# print("Common items:", common_items)
# print("Unique to set1:", unique_to_set1)
# print("Unique to set2:", unique_to_set2)

#reove duplicates from a list using set
# customer_ids = ["C001", "C002", "C001", "C003"]
# unique_customer_ids = set(customer_ids)
# print(unique_customer_ids)

# jan_custimers= {"C001", "C002", "C003"}
# feb_customers= {"C002", "C003", "C004"}
# # repeat_customers= jan_custimers & feb_customers
# # print(repeat_customers)

# new_customers= jan_custimers - feb_customers
# print(new_customers)

# Store_1_sales= [ "C001", "C002", "C001", "C003", "C002", "C001", "C004"]
# Store_2_sales= [ "C003", "C004", "C005", "C003", "C006" ]
# unique_customers= set(Store_1_sales) | set(Store_2_sales)
# print(unique_customers)
# print(f"Total unique customers: {len(unique_customers)}")

# january_customers= {"C001", "C002", "C003", "C004", "C005"} 
# February_customers= {"C003", "C004", "C005", "C006", "C007"}
# March_customers= {"C001", "C003", "C005", "C008"}
# loyal_customers= january_customers & February_customers & March_customers
# print(loyal_customers)

# last_month = {"P001", "P002", "P003", "P004", "P005"}
# current_month = {"P003", "P004", "P005", "P006", "P007", "P008"}
# new_customers = current_month - last_month
# print(new_customers)
# discontnued_customers= last_month - current_month
# print(discontnued_customers)

# north = {"Laptop", "Phone", "Tablet", "Monitor"}
# south = {"Phone", "Tablet", "Speaker", "Headphones"}
# east = {"Laptop", "Monitor", "Keyboard", "Mouse"}
# west = {"Laptop", "Monitor", "Keyboard", "Mouse", "Speaker"}
# universal_products = north | south | east | west
# print("Universal Products:", universal_products)
# north_or_south = north | south
# print("Products in North or South:", north_or_south)
# north_and_south = north & south
# print("Products in North and South:", north_and_south)
# north_not_south = north - south
# print("Products in North but not South:", north_not_south)
# south_not_north = south - north
# print("Products in South but not North:", south_not_north)
# all_product= north ^ south ^ east ^ west
# print("All Products:", all_product)
# all_unique_products= (north | south | east | west) 
# print("All Unique Products:", all_unique_products)
# print(f"Total unique products: {len(all_unique_products)}")

# website_emails = set(["ali@test.com", "sara@test.com", "ali@test.com", "bob@test.com"])
# database_emails = set(["sara@test.com", "charlie@test.com", "ali@test.com"])
# csv_emails = set(["bob@test.com", "ali@test.com", "david@test.com"])
# # all_emails = website_emails | database_emails | csv_emails
# # print(all_emails)

# in_all_sources= website_emails & database_emails & csv_emails
# print(f"Suspicious Emails: {in_all_sources}")

# in_two_sources= (website_emails & database_emails) | (website_emails & csv_emails) | (database_emails & csv_emails)
# print(f"Emails in Two Sources: {in_two_sources}")

# in_two_sources=(database_emails & website_emails) - website_emails
# print(f"Emails in Database and Website but not CSV: {in_two_sources}")

# in_two_sources = (database_emails & csv_emails) - website_emails
# print(f"In DB+CSV but not Website: {in_two_sources}")

# only_website= website_emails - database_emails - csv_emails
# only_database= database_emails - website_emails - csv_emails
# only_csv= csv_emails - website_emails - database_emails
# print(f"Only Website Emails: {only_website}")
# print(f"Only Database Emails: {only_database}")
# print(f"Only CSV Emails: {only_csv}")

# store1_customers = ["C001", "C002", "C001", "C003", "C002", "C001", "C004"]
# store2_customers = ["C003", "C004", "C005", "C003", "C006"]
# unique_customers = set(store1_customers) | set(store2_customers)
# print(f"Total unique customers: {len(unique_customers)}")
# loyal_customers= set(store1_customers) & set(store2_customers)
# print(f"Total loyal customers: {len(loyal_customers)}")
# new_customers= set(store2_customers) - set(store1_customers)
# print(f"Total new customers: {len(new_customers)}")
# new_customers_identified= set(store2_customers) - set(store1_customers)
# print(f"New customers identified: {new_customers_identified}")
# unique_customers = set(store1_customers) ^ set(store2_customers)
# print(f"Total unique customers: {len(unique_customers)}")

# name = "Monni"
# feelings = ["beautiful", "kind", "amazing", "special"]

# print(f"I love everything about {name}:")
# for quality in feelings:
#     print(f"✨ {quality}")


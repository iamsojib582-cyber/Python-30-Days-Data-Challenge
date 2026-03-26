# name=["Sajeeb", "Nami"]
# print(name)
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[-2])
# print(name[0:2])
# print(name[0:2:1])

# fruits=["apple", "banana", "cherry"]
# numbers=[1,2,3,4,5]
# mixed=["apple", 2.4, "banana", 2, True, 3]
# fruits.append("orange")
# print(fruits)
# print(fruits[1])
# print(fruits[1:2])
# print(fruits[0:2:1])
# print(numbers[2])
# print(numbers[:-2])
# print(mixed)
# print(mixed[-1:2:-1])

#Slicing
# country=["Europe", "Asia", "Africa", "North America", "South America"]
# print(country[1:3])
# print(country[0:4:2])
# print(country[0:4:3])
# print(country[::2])
# print(country[-2:])
# print(country[::-1])

# Lists Lenghth 
# name=["sajeeb", "Sanzida", "Monni", "Nami"]
# print(len(name))
# print("Sajeeb" in name)
# print("Sajeeb" not in name)
# print("Sajeeb" in name[0:2])
# print("Sajeeb" in name[1:3])

# Modifying List
# name=["sajeeb", "Sanzida", "Monni", "Nami"]
# name[0]="Sazzad"
# print(name)
# name[1:3]=["Shane", "Sara"]
# print(name)

# Add Items
# division=["Rangpur", "Dhaka", "Khulna", "Chittagong"]
# division.append("Barishal")
# print(division)
# division.insert(2, "Mymensingh")
# print(division)
# division.extend(["Rajshahi", "Sylhet"])
# print(division)

# Remove Items
# division=["Rangpur", "Dhaka", "Khulna", "Chittagong"]
# division.remove("Dhaka")
# print(division)
# division.pop(1)
# print(division)
# division.pop()
# print(division)
# division.clear()
# print(division)

#List methods
# numbers=[1,2,3,4,5,6,7,8,9,10]
# numbers.append(11)
# print(numbers)
# numbers.insert(0, 0)
# print(numbers)
# numbers.append([5,6])
# print(numbers)

# numbers=[5,7,9,11,12]
# numbers.extend([13,14])
# print(numbers)

# letters=["A", "B"]
# letters.extend(["C", "D"])
# print(letters)

# numbers=[5,6,7]
# numbers.insert(0, 0)
# print(numbers)
# numbers.insert(3, 8)
# print(numbers)

# name={"A", "B", "C", "D","E"}
# name.remove("A")
# print(name)
# name.discard("B")
# print(name)
# name.discard("F")
# print(name)

# game=["football", "cricket", "basketball", "volleyball"]
# game.pop(1)
# print(game)
# game.pop()
# print(game)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# numbers.clear()
# print(numbers)

#find positions
# city=["Dhaka", "Rangpur", "Chittagong", "Khulna"]
# print(city.index("Dhaka"))
# print(city.index("Chittagong"))
# position=city.index("Khulna",2)
# print(position)

# count=[1,2,3,1,2,3,1,2,3,2]
# print(count.count(1))
# print(count.count(2))
# print(count.count(3))

# words=["S","M","J","S","M","J","S","M","J"]
# print(words.count("S"))
# print(words.count("M"))
# print(words.count("J"))

# numbers=[10,11,8,7,6,15,14,13,12]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# name=["Sajeeb", "Sanzida", "Monni", "Nami"]
# name.sort()
# print(name)
# name.sort(reverse=True)
# print(name)

# numbers=[10,11,8,7,6,15,14,13,12]
# numbers.reverse()
# print(numbers)

# fruits=["apple", "banana", "cherry"]
# fruits.reverse()
# print(fruits)

# original=[1,2,3,4,5]
# copy=original.copy()
# copy.append(6)
# print(copy)
# print(original)
# list2=original
# list2.append(7)
# print(list2)
# print(original)

# Looping Through Lists
# fruits=["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# for i in range(len(fruits)):
#    print(f"{i}: {fruits[i]}")

# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")

# city=["Dhaka", "Rangpur", "Chittagong", "Khulna"]
# i=0
# while i < len(city):
#     print(f"{i}: {city[i]}")
#     i+=1

# numbers=[1,2,3,4,5]
# squared=[x**2 for x in numbers]
# print(squared)

# numbers= [1,2,3,4,5,6,7,8,9,10]
# even=[x for x in numbers if x%2==0]
# print(even)
# odd=[x for x in numbers if x%2!=0]
# print(odd)

# text=["hellow", "Sajeeb"]
# text2=[x.upper() for x in text]
# print(text2)

# Student Grade Management
# student={
#     "Sajeeb":[84,90,77,69],
#     "Sajid":[56,78,77,69],
#     "Safia":[86,90,66,69],
#     "Sanzida":[87,92,55,69],
#     "Monni":[88,93,44,69],
# }
# for name, grades in student.items():
#     total=sum(grades)
#     average=total/len(grades)
#     print(f"{name}: {grades} → Average: {average:.1f}")

#Shopping Cart
# cart=[]
# while True:
#     print("\n--------- SHopping Cart ---------")
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. View cart")
#     print("4. Exit")
#     print("--" * 20)
#     choice=int(input("Enter your choice (1-4): "))
#     if choice==1:
#         item=input("Enter the item: ")
#         price=float(input("Enter the price: "))
#         cart.append({"item": item, "price": price})
#         print(f"{item} added to cart")
#     elif choice==2:
#         item=input("Enter the item to remove: ")
#         for product in cart:
#             if product["item"] == item:
#                 cart.remove(product)
#                 print(f"{item} removed from cart")
#                 break
#         else:
#             print("Item not found")
#     elif choice==3:
#         print("Cart:")
#         for product in cart:
#             print(f"{product['item']} - ${product['price']}")
#     elif choice==4:
#         print("Goodbye")
#         break
#     else:
#         print("Invalid choice")
        
# Employees List 
# employees=[
#     {"name": "John", "salary": 50000, "department": "HR"},
#     {"name": "Jane", "salary": 60000, "department": "Sales"},
#     {"name": "Bob", "salary": 40000, "department":"IT"},
#     {"name": "Alice", "salary": 55000, "department":"Analystics"},
# ]
# high_earners=[emp for emp in employees if emp["salary"]>50000]
# print("High Earners:")
# for emp in high_earners:
#     print(f"{emp['name']} : ${emp['salary']}")

# staff=[emp["name"]for emp in employees if emp ["department"]== "HR"]
# print(f"\nIT Staff: {staff}")

#list statistics
# score=[60,66,70,80,90,100]
# total=sum(score)
# average=total/len(score)
# highest=max(score)
# lowest=min(score)
# sorted_score=sorted(score)
# print(f"Total: {total}")
# print(f"Average: {round(average,2)}") 
# print(f"Highest: {highest}")
# print(f"Lowest: {lowest}")
# print(f"Sorted: {sorted_score}")

# above_avearge=[x for x in score if x>average]
# print(f"Scores above average: {above_avearge}")

# Duplicates Remover
# numbers=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# unique=list(set(numbers))
# print(unique)

# unique_set=list(set(numbers))
# print(sorted(unique_set),unique_set)

# unique_list=[]
# for num in numbers:
#     if num not in unique_list:
#         unique_list.append(num)
# print(unique_list)

#Inventory Management
# inventory=[
#     {"product": "Laptop", "quantity": 5, "price": 1000},
#     {"product": "Mouse", "quantity": 10, "price": 50},
#     {"product": "Keyboard", "quantity": 8, "price": 75},
#     {"product": "Monitor", "quantity": 3, "price": 200},
#     {"product": "Speaker", "quantity": 6, "price": 150}
# ]
# print("====== Inventory========")
# total_value=0
# for item in inventory:
#     value=item["quantity"]*item["price"]
#     total_value+=value
#     print(f"{item['product']}: {item['quantity']} x ${item['price']} = ${value}")

# print(f"\nTotal Value: ${total_value}")

# low_stock=[item for item in inventory if item["quantity"]<5]
# print("\nLow Stock Items:")
# for item in low_stock:
#     print(item["product"])

#student grades analyzer
# grades=[88,90,91,77,69,56,78,77,69,86,90,66,69,87,92,55,69,88,93,44,69]
# grades2=list(set(grades))
# excellent = len([g for g in grades2 if g >= 90])
# good=len([g for g in grades2 if g>=80 and g<90])
# average=len([g for g in grades2 if g>=70 and g<80])
# poor=len ([g for g in grades2 if g>=60 and g<70])
# fail=len([g for g in grades2 if g<60])
# print("=======Grades Distribution=======")
# print(f"Exellent (90+): {excellent}")
# print(f"Good (80-89): {good}")
# print(f"Average (70-79): {average}")
# print(f"Poor (60-69): {poor}")
# print(f"Fail (60-69): {fail}")

# Top3=[g for g in sorted(grades2,reverse=True)][:3]
# print(f"\nTop 3 Grades: {Top3}")

# Bottom3=[g for g in sorted(grades2)][:3]
# print(f"\nBottom 3 Grades: {Bottom3}")

# grades = []
# print("Enter student grades (type -1 to quit):")
# while True:
#     try:
#         grade = float(input("Grade: "))
#         if grade == -1:
#             break
#         if 0 <= grade <= 100:
#             grades.append(grade)
#         else:
#             print("Please enter a grade between 0 and 100.")
#     except EOFError:
#         print("End of input reached.")
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
# if grades:
#     total = sum(grades)
#     average = total / len(grades)
#     count = len(grades)
#     highest = max(grades)
#     lowest = min(grades)
#     above_average = [g for g in grades if g > average]
#     below_average = [g for g in grades if g < average]
#     sorted_grades = sorted(grades)
#     print("====== Grades Distribution ======")
#     print("Student Summary:")
#     print(f"Total Students: {count}")
#     print(f"Highest Grade: {highest}")
#     print(f"Lowest Grade: {lowest}")
#     print(f"Average Grade: {average:.2f}")
#     print(f"Sorted Grades: {sorted_grades}")
#     print(f"Grades Above Average: {above_average}")
#     print(f"Grades Below Average: {below_average}")
# else:
#     print("No grades entered.")

# To Do List App
# tasks=[]
# while True:
#     print("\n----- Task Manager Menu----")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3.Marks Completed")
#     print("4. Remove Task ")
#     print("5. Exit")
#     choice=input("Enter your choice: ")
#     if choice=='1':
#         new_tasks=input("Enter the tasks descriptions:").strip()
#         if new_tasks:
#             tasks.append({"task": new_tasks, "status": "Pending"})
#             print(f"Task added: {new_tasks}")
#         else:
#             print("Task description cannot be empty")
#     elif choice=='2':
#         if not tasks:
#             print("\n Your Task List is Empty")
#         else:
#             print("\nYour Task List:")
#             for index, task in enumerate(tasks, start=1):
#                start_icon="🟢" if task["status"] == "Completed" else "🔴"
#                print(f"{start_icon} {index}. {task['task']}")
#     elif choice=='3':
#         if not tasks:
#             print("\n Nothing to mark as completed")
#         else:
#             try:
#                 task_num=int(input("Enter the task number to mark as completed: "))
#                 tasks[task_num-1]["status"] = "Completed"
#                 print(f"Task {task_num} marked as completed")
#             except ValueError, IndexError:
#                 print("Invalid task number")
#     elif choice=='4':
#         if not tasks:
#             print("\n Nothing to remove")
#         else:
#             try:
#                 task_num=int(input("Enter the task number to remove: "))
#                 removed=tasks.pop(task_num-1)
#                 print(f"Task {task_num} removed: {removed['task']}")
#             except ValueError, IndexError:
#                 print("Invalid task number")
#     elif choice=='5':
#         print("Goodbye")
#         break
#     else:
#         print("Invalid choice")

# List Operations
# list_1=["Python","Java","C++","C#","Ruby","JavaScript","PHP","SQL","HTML","CSS"]
# list_2=["Python","Java","Power BI","Excel","SQL","HTML","CSS"]
# set_a=set(list_1)
# set_b=set(list_2)
# common=set_a.intersection(set_b)
# unique=set_a.union(set_b)
# merged_unique=list(set_a.union(set_b))
# print(f"List A: {list_1}")
# print(f"List B: {list_2}")
# print("-"*30)
# print(f"Common Items: {common}")
# print(f"Unique Items: {unique}")
# print(f"Merged Unique Items: {merged_unique}")

# Shopping Budget Tracker
shopping_list=[]
print("Enter your items and prices (type 'done' as items name to finish)")
while True:
    item=input("Item name: ") .strip().title()
    if item.lower() == "done":
        break
    try:
        price=float(input(f"Price for {item}: "))
        shopping_list.append({"item": item, "price": price})
    except ValueError:
        print("Invalid price. Please enter a valid number.")
if shopping_list:
    total_cost=sum(item["price"] for item in shopping_list)
    average_price=total_cost/len(shopping_list)
    expensive_items=[item["item"] for item in shopping_list if item["price"] > 50]
    print("\n" + "="*30)
    print("Shopping List:")
    for entry in shopping_list:
        print(f"- {entry['item']}: ${entry['price']:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Average Price: ${average_price:.2f}")
    if expensive_items:
        print(f"Expensive Items: {', '.join(expensive_items)}")
    else:
        print("No expensive items found.")
else:
    print("No items entered.")

    

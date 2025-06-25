
# Marks = {
#     "Harry": 85,
#     "John": 74,
#     "Lisa": 81
# }

# print(Marks)

# print(type(Marks))


# # Properties

# # It is mutable
# # It is Indexed
# # It is unordered
# # It can't contain duplicte values




# # Dictionary Methods

# # Items

# print(Marks.items()) # This method will make seperate list of each key value pair.

# # Keys

# print(Marks.keys()) # This method will give us  the output of only keys not values.

# # Values

# print(Marks.values()) # This method will give us  the output of only Values not keys.

# # Update

# Marks.update({"Harry":88}) # This will update the marks of Harry  Bcz Dictionary is mutable. 
# print(Marks)

# Marks.update({"Marco":90}) # This will add the new pair in our dictionary.
# print(Marks)


# # get

# print(Marks.get("Marco")) # The method will give  us the other value of any  key.
 





#  Dictionary Practice – Level Wise

# 🟢 Level 1: Basics

# Create a dictionary named student with:

# Name: "Ali", Age: 22, Grade: "A"

# Print the dictionary
# Print only the age using key
# Print all keys
# Print all values
# Add a new key Subject with value "Python"
# Then update "Grade" to "A+"


# student = {
#     "Name":"Ali",
#     "Age":22,
#     "Grade":"A"
# }

# print(student)

# print(student["Age"])
# print(student.keys())
# print(student.values())

# print(student.update({"Subject":"Python","Grade":"A+"}))
# print(student)



# # 🟡 Level 2: Dictionary Logic
# # Given:
# # marks = {
# #     "Math": 80,
# #     "Science": 70,
# #     "English": 90
# # }

# # Print total marks
# # Add a new subject: "History": 75
# # Check if "Urdu" is in the dictionary or not

# marks = {
#     "Math": 80,
#     "Science": 70,
#     "English": 90
# }

# print(marks)                                                # Print total marks

# print(marks.update({"History":75}))                      # Add a new subject: "History": 75

# print("Urdu" in marks)                                          # Check if "Urdu" is in the dictionary or not



# # 🔴 Level 3: Brain Booster
# # Create an empty dictionary contacts
# # Ask user to enter 3 names and phone numbers
# # Add them to the dictionary as key-value pairs
# # Print the final dictionary

# contacts = {}  # ✅ Empty dictionary

# # Input 3 contacts
# name1 = input("Enter name 1: ")
# phone1 = input("Enter phone 1: ")

# name2 = input("Enter name 2: ")
# phone2 = input("Enter phone 2: ")

# name3 = input("Enter name 3: ")
# phone3 = input("Enter phone 3: ")

# # Add to dictionary
# contacts[name1] = phone1
# contacts[name2] = phone2
# contacts[name3] = phone3

# print("Contacts saved:")
# print(contacts)






# contacts = {}  # Empty dictionary

# for i in range(3):
#     name = input(f"Enter name {i+1}: ")
#     phone = input(f"Enter phone number for {name}: ")
#     contacts[name] = phone  # Add to dictionary

# print("📞 Final Contact List:")
# print(contacts)





# Dictionary Practice (Set 2)

#  Q1. Dictionary Info
# Create a dictionary called info:

# info = {
#     "name": "Uzair",
#     "age": 24,
#     "city": "Lahore"
#     }
# Print only the name
# Add "email": "uzair@email.com"
# Update age to 25
# Print keys and values

# info = {
#     "name": "Uzair",
#     "age": 24,
#     "city": "Lahore"
#     }

# print(info["name"])                                     # Print only the name

# info.update({"email":"uzair@email.com"})        # Add "email": "uzair@email.com"

# info.update({"age":25})                         # Update age to 25

# print(info.keys())

# print(info.values())




# # 🟡 Q2. Word Count Dictionary
# # Take a string from the user like: "python is fun"
# # Count how many times each word appears
# # Store result in a dictionary
# # Hint: Use split() and loop

# sentence = input("Enter a sentence: ")  # You can use static string too
# words = sentence.split()  # Break into list

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)


# # 🟠 Q3. Marks Checker

# # students = {
# #     "Ali": 87,
# #     "Sana": 92,
# #     "Usman": 76
# # }
# # Ask user to enter a name
# # If the name exists, print marks
# # Else print: "Student not found"


# students = {
#      "Ali": 87,
#      "Sana": 92,
#     "Usman": 76
# }

# name_check = input("Enter any name: ")

# if name_check in students:
#      print(f"{name_check} got {students[name_check]} marks")
# else:
#     print("Student not found")





# # 🔵 Q4. Menu System (Basic Dictionary App)
# # Create a dictionary:

# # menu = {
# #     "burger": 200,
# #     "pizza": 500,
# #     "fries": 100
# # }
# # Ask user to enter an item
# # Print the price
# # If item not found, print "Item not available"

# menu = {
#     "burger": 200,
#     "pizza": 500,
#     "fries": 100
# }

# item_check = input("Enter any item: ")

# if item_check in menu:
#     print(f"Price of {item_check} is Rs.{menu[item_check]}")
# else:
#     print("Item not available")



# # 🔴 Q5. Loop + Dictionary
# # Create an empty dictionary.
# # Loop 5 times and take user input (fruit name and quantity).
# # Example:
# # Apple → 5  
# # Banana → 10  
# # Store as:

# # {
# #     "Apple": 5,
# #     "Banana": 10
# # }
# # Then print full fruit stock dictionary.


# fruit_stock = {}

# for i  in range(5):
#     fruit = input(f"Enter fruit {i+1}: ")
#     Quantity = int(input(f"Enter fruit quantity here for {fruit}: "))
#     fruit_stock[fruit] = Quantity

# print(fruit_stock)

































# Mentor’s Special Practice Set – Mix of Logic + Fun

#  Q1. Basic Dictionary – Book Info
# Create a dictionary called book:
# {
#     "title": "Python 101",
#     "author": "Ali",
#     "pages": 250
# }

# Print title and pages only
# Add "publisher": "CodeHouse"
# Update pages to 300
# Print all values


Book = {
    "title": "Python 101",
    "author": "Ali",
    "pages": 250
}

print(Book["title"])
print(Book["pages"])

Book.update({"publisher": "CodeHouse"})
Book.update({"pages":300})
print(Book)



#  Q2. Login System
# Create a dictionary:

# users = {
#     "admin": "1234",
#     "user1": "pass1",
#     "user2": "hello123"
# }
# Ask user to:
# Enter username and password
# If both match, print "Login successful!"
# Else, print "Invalid credentials"

users = {
    "admin": "1234",
    "user1": "pass1",
    "user2": "hello123"
}

user_check = input("Enter username: ")
password_check = int(input("Enter password: "))

if user_check in users and users[user_check] == password_check:
    print("Login Successful")
else:
    print("Invalid credentials")





#  Q3. Quiz Score Tracker
# Make an empty dictionary scores = {}
# Then loop 3 times:

# Ask user for student name and marks
# Store each in the dictionary
# After loop, print dictionary
# Also print total score of all students

scores = {}

for i in range(3):
    student_name = input(f"Enter name of student {i+1}: ")
    student_marks = int(input(f"Enter  marks of student {student_name}: "))
    scores[student_name] = student_marks

print(scores)
print(sum(scores.values()))






#  Q4. Price Calculator with Dictionary
# Make a price list:

# prices = {
#     "tea": 50,
#     "coffee": 80,
#     "cookie": 30
# }

# Ask user for an item
# If found, ask for quantity, calculate total
# If not found, print "Not available"

prices = {
    "tea": 50,
    "coffee": 80,
    "cookie": 30
}
item = input("Enter any item here: ")

if item in prices:
    qty = int(input("enter quantity  here: "))
    total = qty * prices[item]
    print("Total Price:", total)
else:
    print("Not available")





#  Q5. Dictionary + Count
# Take a sentence input from the user.
# Count how many times each letter appears (not words)
# Ignore spaces
# Store result in dictionary and print it
# Example input: "hello world"
# Expected output:
# {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

sentence = input("Enter any sentence: ")
sentence = sentence.replace(" ", "")  # Remove spaces

letter_count = {}

for char in sentence:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print(letter_count)

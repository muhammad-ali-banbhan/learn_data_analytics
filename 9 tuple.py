

#  Tuple

tple = (2, 3, "Ali",3,66,False, 33.55)
print(tple)
print(type(tple))



# Tuple Methods

#  Count

print(tple.count("Ali"))
print(tple.count(3))


# Index

print(tple.index(66))




# Tuples Practice Set – Beginner to Strong

# Create a tuple named fruits containing: "apple", "banana", "mango", "banana"
# Print the tuple
# Print the type of fruits
# Count how many times "banana" appears
# Find the index of "mango"

fruits = ("apple", "banana", "mango", "banana")
print(fruits)                     # Print the tuple
print(type(fruits))                  # Print the type of fruits
print(fruits.count("banana"))           # Count how many times "banana" appears
print(fruits.index("mango"))                # Find the index of "mango"     


# Make a tuple called mixed with different types of data:
# An integer, a float, a string, and a boolean
# Then print each element using indexing

mixed = (22, 44,33.77, "Khan", "Uzair", False, None)
print(mixed[0:7])


# Can you change the value of a tuple? Try this:

# test = (1, 2, 3)
# test[1] = 5
# print(test)

# test  = (1,2,3)
# test[1] = 5 # This wll  give the error in output bcz Tuple is unmutable.
# print(test) 






# Tuple slicing:

# data = (10, 20, 30, 40, 50, 60)
# Print first 3 elements
# Print last 2 elements using negative indexing
# Print middle 3 elements

data = (10, 20, 30, 40, 50, 60) 
print(data[0:3])                        # Print first 3 elements
print(data[-2])                     # Print last 2 elements using negative indexing
print(data[1:4])                    # Print middle 3 elements




# Take a tuple of numbers:

# numbers = (5, 10, 15, 20, 25)
# Ask user to enter a number
# Check if it exists in the tuple
# If yes → print "Yes, it exists"
# Else → print "No, not found"


numbers = (5, 10, 15, 20, 25)
num = int(input("Enter any number:"))
if num in numbers:
    print("Yes, it exists")
else:
    print("No, not found")



# Tuples Practice Set – Round 2

# Q1. Create & Access
# Create a tuple info = ("Ali", 25, "Karachi", True)
# Print the full tuple
# Print only the city
# Print the last element using negative indexing
# Print the first two elements using slicing

info = ("Ali", 25, "Karachi", True)

print(info)             # Print the full tuple

print(info[2])            # Print only the city


print(info[-2])         # Print the last element using negative indexing


print(info[0:2])        # Print the first two elements using slicing




# Q2. Tuple + Condition
# Given:
# nums = (4, 8, 15, 16, 23, 42)
# Check if 23 exists in tuple → print "Yes"
# Check if 99 exists → print "Not Found"
# Print the sum of all values in the tuple


nums = (4, 8, 15, 16, 23, 42)

if 23 in nums:
    print("Yes")
else:
    print("Not Found")

print("Sum:",sum(nums))



# # Q3. Tuple + Loop (Harder Logic)
# Tuple:
# data = (5, "apple", 6.6, True, "banana", None, 99)
# Loop through the tuple and print only integers
# Print how many string values are present in the tuple

data = (5, "apple", 6.6, True, "banana", None, 99)

# Print only integers
for item in data:
    if type(item) == int:
        print("Integer:", item)

# Count string values
string_count = 0
for item in data:
    if type(item) == str:
        string_count += 1

print("Total strings:", string_count)



#  Q4. Tuple Packing & Unpacking
# Pack these values into a tuple:
# name = "Uzair"
# age = 21
# city = "Sukkur"
# Then unpack the tuple into 3 variables and print like:
# "Uzair is 21 years old from Sukkur."



# Packing
person = ("Uzair", 21, "Sukkur")

# Unpacking
name, age, city = person

print(f"{name} is {age} years old from {city}.")

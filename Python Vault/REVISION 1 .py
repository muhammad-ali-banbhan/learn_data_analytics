
# #  Practice Set – Revision Mode
# # 🟢 Level 1: Easy Warm-up

# # Create 3 variables: name = "Ali", age = 22, height = 5.9.
# # Print a sentence using them like:
# # 👉 Ali is 22 years old and 5.9 feet tall.
# name  = "Ali"
# age = 23
# height  = 5.9
# print(f"{name} is {age} old and {height} feet tall")

# # Take 2 numbers from the user and print their:
# # Sum
# # Difference
# # Multiplication
# # Division
# num1 = int(input("Enter the number 1 here: "))
# num2 = int(input("Enter the number 2 here: "))

# print("Sum:", num1 + num2)
# print("Remainder:", num1 % num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)


# # Given a string "Programming", print:
# # First 4 characters
# # Last 4 characters
# # Middle 3 characters

# word = "Programming"
# print(word[0:4])
# print(word[7:11])
# print(word[4:7])



# # 🟡 Level 2: Intermediate Logic
# # List: marks = [45, 67, 89, 34, 76]
# # Print the second highest number
# # Insert 99 at index 2
# # Remove the lowest number
# # Sort the list in descending order

# marks = [45,67,89,34,76]
# print(marks)

# sorted_marks = sorted(marks, reverse=True) # the second highest number.
# print("Second highest:", sorted_marks[1])

# marks.insert(2, 99)   # insert 99 at index 2.
# print(marks)
# marks.remove(34) # remove the lowest number.
# print(marks)
# marks.sort(reverse=True) # Sort the list in descending order
# print(marks)


# # text = "Python Is Fun"
# # Convert to all lowercase
# # Replace "Fun" with "Powerful"
# # Print only the word "Is" using slicing

# text = "Python Is Fun"
# print(text.lower())
# print(text.replace("Fun" ,"Powerful"))
# print(text)
# print(text[7:9])


# # Take a number from the user.
# # Print if it's even or odd
# # Also print its square and cube


# number = int(input("Enter any number here: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# print(number**2) # the square of the number.
# print(number**3) #  the cube of the number.



# # 🔴 Level 3: Brain Booster
# # List: mix = [12, "Ali", 5.5, True, None, "Python"]
# # Print only the string values from the list
# # Replace "Ali" with "Ahmed"
# # Count how many elements are int or float

# mix = [12, "Ali", 5.5, True, None, "Python"]

# # Print only the string values from the list
# for item in mix:
#     if type(item) == str:
#         print(item)

# # Replace "Ali" with "Ahmed"
# mix[1] = "Ahmed"
# print(mix)

# # Count how many elements are int or float
# count = 0
# for item in mix:
#     if type(item) in [int, float]:
#         count += 1
# print("Count of int/float:", count)


# # Take a user name input. If the name is "admin", print "Welcome, Admin!"
# # Otherwise, print "Welcome, Guest!"

# NAME = input("Enter any name here: ")

# if NAME.lower() == "admin":
#     print("Welcome, Admin!")
# else:
#     print("Welcome, Guest!")






# Revision Practice Set – Round 2 (Mixed Level)

# Q1. String Logic
word = "DataScience"
# Print only "Data"
# Print only "Science"
# Replace "Data" with "AI" and print result
# Check if "Sci" is present in the word

print(word[0:4]) # Print only "Data"

print(word[4:11]) # Print only "Science"

print(word.replace("Data","AI"))  # Replace "Data" with "AI" and print result

# Check if "Sci" is present in the word


# Q2. User Input + Condition
# Take 2 numbers from user
# Print "Both are even" if both are even
# Print "One is odd" if only one is odd
# Else print "Both are odd"

num1 = int(input("enter any number here: "))
num2 = int(input("enter any  number here:  "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both are odd")
else:
    print("One is odd")


# Q3. List + Logic
items = ["pen", "pencil", "eraser", "scale", "sharpener"]
# Print total number of items
# Check if "marker" is in the list or not
# Replace "eraser" with "highlighter"
# Sort the list alphabetically and print


print(len(items)) # Print total number of items

print("marker" in items) # Check if "marker" is in the list or not

index = items.index("eraser")   # Replace "eraser" with "highlighter"
items[index] = "highlighter"
print(items)

items.sort(reverse=False) # Sort the list alphabetically and print
print(items) 



# # Q4. Math Operation
# Take a float number from user
# Print:
# Round off value using round()
# Floor value using int()
# Its square root (hint: use exponent **)

float_number = float(input("Enter the float number"))

print(round(float_number))     #  Round
print(int(float_number))       #  Floor
print(float_number ** 0.5)     #  Square root


# Q5. Bonus Brain
# Ask user to enter a sentence (string)
# Print total number of characters
# Print how many times letter "a" appears
# Convert whole sentence to UPPERCASE
# Print only the last 5 characters

sentence = input("Enter a sentence: ")

print("Total characters:", len(sentence))             # Print total number of characters

print("Count of 'a':", sentence.lower().count("a"))   #  Print how many times letter "a" appears

print("UPPERCASE:", sentence.upper())                 # Convert whole sentence to UPPERCASE

print("Last 5 characters:", sentence[-5:])            # Print only the last 5 characters


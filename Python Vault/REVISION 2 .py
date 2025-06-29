# Python Revision Practice Set (Level 1 & 2)
# By: Muhammad Ali Banbhan


# -----------------------------
# Q1. Create 3 variables and print in formatted sentence
name = "Ali"
age = 22
city = "Lahore"

# Print formatted output
print(f"{name}, aged {age}, lives in {city}.")





# -----------------------------
# Q2. Take 2 float numbers from user and show operations
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# Sum
print("Sum:", num1 + num2)
# Product
print("Product:", num1 * num2)
# Rounded values
print("Rounded Number 1:", round(num1))
print("Rounded Number 2:", round(num2))







# -----------------------------
# Q3. String slicing
Word = "Programming"
# Print "gram" (index 3 to 6)
print(Word[3:7])
# Print last 3 characters using negative indexing
print(Word[-3:])






# -----------------------------
# Q4. List operations
List = [10, 5, 15, 20]
# Add 25 to end
List.append(25)
# Remove 5
List.remove(5)
# Print middle 2 values (index 1 and 2)
print(List[1:3])







# -----------------------------
# Q5. Tuple indexing and types
Tuple = (5, "Ali", 7.5, True)
# Print type of each element
print(type(Tuple[0]))
print(type(Tuple[1]))
print(type(Tuple[2]))
print(type(Tuple[3]))
# Print first 2 elements using slicing
print(Tuple[0:2])






# -----------------------------
# Q6. Dictionary operations
Dictionary = {"Math": 75, "English": 88, "Science": 91}
# Add Urdu subject
Dictionary.update({"Urdu": 85})
# Update English marks
Dictionary.update({"English": 90})
# Print updated dictionary
print(Dictionary)






# -----------------------------
# Q7. FizzBuzz logic
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)






# -----------------------------
# Q8. String methods practice
String = "DataScience"
# Count letter 'e'
print("Count of 'e':", String.count("e"))
# Convert to uppercase
print("Uppercase:", String.upper())
# Replace Science with Analytics
print("Replaced:", String.replace("Science", "Analytics"))





# -----------------------------
# Q9. Take 3 fruits and quantities from user
fruit_dict = {}
for i in range(3):
    fruit = input(f"Enter fruit name {i+1}: ")
    quantity = int(input(f"Enter quantity for {fruit}: "))
    fruit_dict[fruit] = quantity
# Print full dictionary
print("Fruit stock:", fruit_dict)
# Print total quantity
print("Total quantity:", sum(fruit_dict.values()))





# -----------------------------
# Q10. Count letters in a sentence
Sentence = input("Enter a sentence: ")
Sentence = Sentence.replace(" ", "")  # Remove spaces
letter_count = {}
for char in Sentence:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
# Print letter counts
print("Letter frequency:", letter_count)








# Revision Practice Set – Level 3

# Q1. Data Summary (Mix of Variables + Strings + Input)

# Take user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course name: ")

# Print formatted message
print(f"{name}, aged {age}, is enrolled in the {course} course.")





# Q2. Smart Calculator (Input + Operators)

# Take inputs
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation based on operator
if operator == '+':
    print("Result:", number1 + number2)
elif operator == '-':
    print("Result:", number1 - number2)
elif operator == '*':
    print("Result:", number1 * number2)
elif operator == '/':
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator!")





# Q3. List Filter

# Given list of numbers
nums = [12, 7, 15, 2, 18, 5, 10]

# Filter even numbers
even_nums = [n for n in nums if n % 2 == 0]

# Filter odd numbers
odd_nums = [n for n in nums if n % 2 != 0]

# Sum of even numbers
sum_even = sum(even_nums)

# Output results
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
print("Sum of even numbers:", sum_even)





# Q4. Dictionary – Student Result

# Dictionary with student marks
result = {
    "Ali": 85,
    "Sana": 90,
    "Usman": 76
}

# Ask user for a name
name_check = input("Enter student name: ")

# Check and print result
if name_check in result:
    print(f"{name_check} got {result[name_check]} marks.")
else:
    print("Student not found!")






# Q5. Tuple Loop + Type Count

# Mixed data tuple
mix = (10, "Hi", 5.5, True, None, "Python", 22)

# Counters for each type
int_count = 0
str_count = 0
bool_count = 0

# Loop through each item and count types
for item in mix:
    if isinstance(item, bool):
        bool_count += 1
    elif isinstance(item, int):
        int_count += 1
    elif isinstance(item, str):
        str_count += 1

# Output counts
print("Total integers:", int_count)
print("Total strings:", str_count)
print("Total booleans:", bool_count)

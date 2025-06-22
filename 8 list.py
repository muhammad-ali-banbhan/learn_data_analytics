
#  In list we  can  store any type of data.

my_list = ["Apple",  55,  0.5,  True, None,  "Khan"]
print(my_list)


print(my_list[3])

print(my_list[0])

#   list values can be  change which means list are mutable.

my_list[0] = "Banana"
print(my_list[0])

print(my_list)


#  list Indexing

print(my_list[1:3])


#   LIST METHODS

# append
my_list.append("Chicken")
print(my_list)

#  Sort
numbers = [1,3,5,2,6,8,5,9]
numbers.sort()
print(numbers)

#  Reverse
numbers.reverse()
print(numbers)

# Insert
my_list.insert(4,"Patato")
print(my_list)

# POP
numbers.pop(4)
print(numbers.pop(4))
print(numbers)

#  Remove
numbers.remove(2)
print(numbers)





# Practice Questions (List):

# Create a list of 5 cities and print only the first 3.

cities =  ["Karachi","Hyderabad","Sukkur","Khairpur","Ghotki"]
print(cities)
print(cities[0:3])

# Add a new city at the end using append().

cities.append("MirpurKhas")
print(cities)

# Replace the 2nd city with "Islamabad".

# print(cities.replace("Hyderabad","Islamabad"))

#  Error: list object has no attribute replace
# 📌 replace() is for strings, not lists

cities[1] ="Islamabad"
print(cities)

# Remove the last item using pop().
cities.pop()
print(cities)

# Reverse the list and print it.

cities.reverse()
print(cities)
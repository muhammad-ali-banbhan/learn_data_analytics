
name = "Neymar"

print(name)
print(len(name)) # it will  print the length of characters in  this  name.

print(name[1:3]) # this is indexing

nameshort = name[0:3]    # this will give us the output of some characters  that  we want this is bcz of indexing.
print(nameshort)


check_character = name[1] # this  will tells us that  whiich  letter/character is on 1 number or  we can give the number acc to  our length.
print(check_character)



#  there are indexing slicing which  means  the characters on numbers 
#  in positive slicing  it always start   with 0 and end on any  number acc to length of  out word.
#  but in  negative slicing it always start with -1 and end on any negative number acc to aaur words length.

#  Example 

NAME = "Messi"
print(NAME)

print(len(NAME))# if we  want  to check  the length of our name.

print(NAME[1:4])  # it  will  print out the  characters of our name which will on number 1 , 2, 3 but not number 4 it always exclude the last number we give it in positive indexing.
print(NAME[-4:-1])  #  it will print out the haracters of our name which will on number 1 , 2, 3 but not number 4 it always exclude the last number we give it in negative indexing.

print(NAME[:4])  # if we didnot give the first number of indexing that  we want in output and  give it only 2nd nuumber it will always assume it from 0  to  other character that we give it.
print(NAME[1:]) # if we didnot give the second number of indexing same it will assume till  the last character of lenth  of  our word.



# | Expression | Meaning                           |
# | ---------- | --------------------------------- |
# | `s[1:4]`   | index 1 se 3 tak (4 excluded)     |
# | `s[-4:-1]` | negative indexing (last excluded) |
# | `s[:4]`    | start se index 3 tak (0 to 3)     |
# | `s[1:]`    | index 1 se end tak                |



# PRACTICE

# word = "Python"
# Print only: yth using slicing, Print last 3 characters using negative slicing.

word = "Python"
print(word)
print(word[1])
print(word[-3 :])


# city = "Karachi"
# Print first 4 letters using slicing. Print "chi" using negative slicing.

city = "Karachi"
print(city)
print(city[0:4])
print(city[-3:])


# fruit = "Banana"
# Print "ana" from the middle. Print "Ban" using [:3]

fruit = "Banana"
print(fruit)
print(fruit[1:4])
print(fruit[:3])






#  SKIP VALUE SLICING

numbers = "12345678910"
print(numbers)
print(numbers[0:5:2])
print(numbers[0:5:3])

print(numbers[0:7:2])
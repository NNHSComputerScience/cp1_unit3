# For Loops and Sequences Notes

# SEQUENCE = An ordered list of elements, like a string or range.
#   e.g. range(5) is an ordered list of numbers: 0,1,2,3,4
#   e.g. the string "hello" != "olleh"

# ELEMENT = A single item in a sequence.
#   e.g. the "h" in "hello"

# ITERATE = To step through a sequence, in order, and one element at a time.

# FOR LOOP = Iterates through a sequence, and executes the loop body for each element in the sequence.

for letter in "Computer Science":
    print (letter, end="")

# Often i is used as the looping variable (convention used by many programmers, originating from mathematics)
for i in range(5):
    print (i, end="")

# CHALLENGE: Secret Message - Ask the user for a message and the display it with each letter displayed twice.
#       e.g. if the message is "great", the output is "ggrreeaatt"
message = input("\nPlease enter a message: ")
for i in message:
    print (i*2, end="")

# Quick Question: What would display?
string = "Ha"
for letter in string:
    print (string,end="")
print ()

# ANSWER: HaHa

# The built-in len() function:
#   returns the number of elements in a sequence as an integer.

word = "Bananas"
print (len(word))
print(len(range(5)))

# CHALLENGE: Save your first and last name as a string, and then display
#   how many letters are in your full name. What did you learn?

name = "Matt Callaghan"
print (name, "is", len(name), "elements long.")
print ()

#ANSWER: len() counts the spaces!

# "in" and "not in" operators 
#   can check to see if an element is or is not in a sequence and return a boolean.
print("the 'in' operator:")
if "a" in name.lower():
    print ("Awesome, you have an A!")
else:
    print ("You don't have an A.")
    
print("the 'not in' operator:")
if "e" not in name.lower():
    print ("You don't have an E.")
else:
    print ("Awesome, you have an E!")

# CHALLENGE: Password
#       Ask the user for a password. It must be at least 6 characters long,
#       and it must contain a '!' or a '$' sign. If they give a valid password
#       display "Valid Password", otherwise display "Invalid Password".
print("\nPlease enter a password that's >6 characters long and contains a '!' or '$'.")
password = input("What is your password: ")
if ("!" in password or "$" in password) and len(password) >= 6:
    print ("Valid Password")
else:
    print ("Invalid Password")

# Adv. CHALLENGE: Can you use a while loop to keep asking for the password
#       until the user enters it in the correct format?
print("\nPlease enter a password that's >6 characters long and contains a '!' or '$'.")
password = input("What is your password: ")
while (("!" not in password) and ("$" not in password)) or len(password)<6:
    print("Invalid password. Please try again.")
    password = input("What is your password: ")
print("Valid Password.")

# type TUPLE: a type of immutable sequence, like a string or range, but can contain ANY type of element.
#   e.g. (0, "a", 2.2, "b", 3, "c")
# IMMUTABLE: once created, cannot be changed

# DATA STRUCTURE: a way of storing and organizing multiple pieces of information(data) in a program; e.g. a tuple

empty_tuple = ()
boys = ("Jim", "John", "Bob", "Alex")
girls =  ("Jill", "Stacy", "Sarah", "Gwendolyn", "Alex")

# printing a tuple
print (boys)
print (girls)

# printing one at a time
for boy in boys:
    print(boy)

# finding one to print (simple search algorithm)
for girl in girls:
    if girl == "Sarah":
        print(girl)
    
# CHALLENGE: search to find name(s) that are in both tuples (modified search algorithm)
for boy in boys:
    if boy in girls:
        print (boy, "is in both tuples")
        
for boy in boys:
    for girl in girls:
        if boy == girl:
            print("Found a duplicate:", boy)

# The tuple() function 
#   Converts any sequence to type tuple.
nums = tuple(range(1,11))
letters = tuple("abcdefg")
print("Printed tuples:\n")
print(nums)
print(letters)


input("\nPress enter to exit.")

# unit 3 notes - turtles & indexing
#   turtle objects and methods
#   indexing a sequence

import turtle

# INDEX VALUE - selects an item from a sequence, such as a character from a string, or an element from a tuple.
#   use square bracket [] to select an item by index value
"""
               0  1  2  3  4  5     ( positive indices start at 0, always the first element )
    string = " T  U  R  T  L  E "
              -6 -5 -4 -3 -2 -1     ( negative indices end at -1, always the last element )
"""

string = "TURTLE"
print("T:", string[0]) # 0 always the first element
print("U:", string[1])
print("R:", string[2], string[-4])
print("T:", string[-3], string[3])
print("L:", string[-2])
print("E:", string[-1]) # -1 always the last element
#print(string[len(string)])  # INDEX ERROR - index out of range; len returns 4

#            0           1            2              3
NAMES = ("Leonardo", "Raphael", "Michelangelo", "Donatello") # all caps variables (CONSTANTS) never change
COLORS = ("blue",    "red",     "orange",       "purple")

# CHALLENGE: print "Leonardo is the color blue" using indexing
print(names[0] + " is the color " + colors[0])

print()
# accessing index values within an loop
#   EXTREMELY common line of code to access index values of one or more sequences
for index in range(len(names)):
    print(names[index] + " is the color " + colors[index])

# Object Oriented Programming (OOP) refresher 
#   OBJECT - a software model that bundles data and behavior together; useful for modeling real-world objects, like turtles!
#   METHOD - behaviors, or actions, of a software object
#       RECALL: Think of and write down below one example of an object in Alice. 
#               Write down two examples of methods for this object.
#       e.g. in Alice a <penguin> was an object and a <penguin's> methods included <"say" and "move">
#       e.g. in Python a <Turtle> is an object and a turtle's methods include moving <forward() & right()>

# create Leonardo
leo = turtle.Turtle()   # create Turtle object from turtle module by calling the class Turtle
# I didn't write the code for a Turtle. How do I know how to use it?
#   Google "Python docs turtle" for Turtle documentation
leo.shape("turtle")     # run method on object to change shape
leo.color(colors[0])    # run method on object to change color

# create Michelangelo
mikey = turtle.Turtle()
mikey.shape("turtle")
mikey.color(colors[2])
mikey.right(180)

# INDIVIDUAL CHALLENGE: create Raphael & Donatello and draw 2 more squares
# create Raphael
raph = turtle.Turtle()
raph.shape("turtle")
raph.color(colors[1])

# create Donatello
don = turtle.Turtle()
don.shape("turtle")
don.color(colors[3])
don.right(180)

# moving a turtle
leo.forward(100)
leo.right(90)
leo.forward(100)

# PARTNER CHALLENGE: use a for loop to draw a square with Leo
for i in range(4):
    leo.forward(100)
    leo.left(90)
    mikey.forward(100)
    mikey.left(90)
    raph.forward(100)
    raph.right(90)
    don.forward(100)
    don.right(90)

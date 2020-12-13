# unit 3 notes - turtles & indexing
#   turtle objects and methods
#   indexing a sequence

import turtle

# INDEX VALUE - selects an item from a sequence, such as a character from a string, or an element from a tuple.
#   Use square brackets (e.g. []) to select an item by index value
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
# INDEX ERROR - index value accesed is out of range or does not exist
#print(string[len(string)])  # len returns 6, but last index value is 5; 

#            0           1            2              3
NAMES = ("Leonardo", "Raphael", "Michelangelo", "Donatello") # all caps variables (CONSTANTS) never change
COLORS = ("blue",    "red",     "orange",       "purple")

# CHALLENGE: print "Leonardo is the color blue" using indexing
print(names[0] + " is the color " + colors[0])

print()
# accessing index values within an loop
#   EXTREMELY common line of code to access index values of a sequence
#   Useful for printing sequences of equal length in columns
for index in range(len(names)):
    print(names[index] + " is the color " + colors[index])

# Object Oriented Programming (OOP) refresher 
#   OBJECT - a software model that bundles data and behavior together; useful for modeling real-world objects, like turtles!
#   METHOD - behaviors, or actions, of a software object (a turtle can move forward, turn right, or change its color)
#   ATTRIBUTES - charactaristics, or data, associated with an object (AKA instance variables) (a turtle has a color, a position, and shape)

# create Leonardo
leo = turtle.Turtle()   # create Turtle object from turtle module by calling the class Turtle
# We didn't write the code for a Turtle. How do we know how to use it?
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

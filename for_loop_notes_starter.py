"""
Name: 
Title: Unit 3 Notes: For Loops 
Description: Overview of using for loops with sequences (strings, ranges, tuples)

FOR LOOP - Our second logical structure for repetition. A for loop iterates through a sequence, and executes the loop body for each element in the sequence. Ends after each item has been accessed. 

# for loop pseudocode:
# for [loop variable] in [sequence]:      
#   repeat statements for each item in sequence
"""

# Comparing for loops to while loops:
print("Print 0-9 using a while loop:")


print("\nPrint 0-9 using a for loop")

 
# LOOP VARIABLE - 


# SEQUENCE - 


# ELEMENT - 


# 2 new sequences: RANGE and TUPLE
	
# RANGE - Built-in function range() returns an immutable sequence of integers of type RANGE. 
#   Accepts 3 arguments: range( [start], end(exclusive), [step] )

print("\nDisplay numbers 1-10:")
 
 
print("\nCount 10-20, by 2's:")


print("\nCount backwards:")


# TUPLE: a type of immutable sequence, like a string or range, but can contain ANY type of element.
#   e.g. (0, "a", 2.2, "b", 3, "c")


print("\nList of students:")


print("\nList of exam scores:")


# The built-in len() function:


# simple search algorithms:


# The tuple() function - 


# Application Challenges:
"""
Bug Collector Program -
   A bug collector collects bugs every day for 7 days. Write a program that keeps a running total of the number of bugs collected during the 7 days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected. Can you get the day number to display each day?
 
Calories Burned Program-
   Running on a treadmill you burn 3.9 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes. Display the number of minutes without hard-coding them.
 
Pennies For Pay Program-
   Write a program that calculates the amount of money a person would earn over a period of time if their salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days worked. Display a table showing what the salary was for each day, and then show the total pay at the end of the period.


Password challenge
   Ask the user for a password. It must be at least 6 characters long, and it must contain a '!' or a '$' sign. If they give a valid password display "Valid Password", otherwise display "Invalid Password". Use a while loop to keep asking for the password until the user enters it in the correct format?
"""

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
count = 0
while count < 10:
	print(count)
	count += 1

print("\nPrint 0-9 using a for loop")
for count in "0123456789":  # for statement
    print (count)	 # loop body
 
# LOOP VARIABLE - Initialized to the first element in the sequence in the for statement and then accesses each subsequent element, one after the other.

print("\nLoop variable:", count)  # loop variable exist outside loop! (notice the value is 9)

chars = 0
word = "\nComputer Science"
for i in word:
	chars += 1
# spaces and escape characters count as 1 character
print(word, "is", chars, "characters long")

# !!! INSTRUCTOR NOTE: peer instruciton #1.1 - 1.3

# SEQUENCE = An ordered list of elements.
#	e.g. A string is an ordered list of characters. The string "hello" != "olleh".

# ELEMENT = A single item in a sequence.
#   e.g. the "h" in "hello"

if ("i" not in "team") and ("u" in "fun"):
	print("\nThese are True!")

# 2 new sequences: RANGE and TUPLE
	
# RANGE - Built-in function range() returns an immutable sequence of integers of type RANGE. 
#   Accepts 3 arguments: range( [start], end(exclusive), [step] )

range_of_nums = range(5) # end only
range_of_nums = range(1,6) # start and end
range_of_nums = range(1,6,2) # start, end, and step
print("Printed range object:", range_of_nums)
print("Type of object:", type(range_of_nums))
print("Range values generated: ", list(range_of_nums))

print("\nDisplay numbers 1-10:")
for num in range(1,11):
    print(num)   
 
print("\nCount 10-20, by 2's:")
nums = range(10, 21, 2) 
for num in nums:
    print(num)

print("\nCount backwards:")
for i in range(10,-11,-3):
    print(i)

# 'i' is used by many programmers as a looping variable (convention originating from mathematics).

# !!! INSTRUCTOR NOTE: peer instruction #2

# TUPLE: a type of immutable sequence, like a string or range, but can contain ANY type of element.
#   e.g. (0, "a", 2.2, "b", 3, "c")

empty_tuple = ()
students = ("Jill", "John", "Sarah", "Bob", "Alex")
scores = (88, 95, 65, 77, 100)

# printing a tuple
print("\nStudent tuple:", students)
print("Exam scores tuple:", scores)

print("\nList of students:")
for stu in students:
    print(stu)

print("\nList of exam scores:")
for score in scores:
	print(score)

# The built-in len() function:
#   returns the number of elements in a sequence as an integer.

num_stus = len(students)
print("\nThere are", num_stus, "students in the class.")

# simple search algorithms
for stu in students:
	if len(stu) > 4:
		print(f"\n{stu}'s name is greater than 4 letters long.")
		
a = 0
for score in scores:
	if score >= 90:
		a += 1
print("\nNumber of A's on the exam:", a)

# The tuple() function - converts any sequence to type tuple.
nums = tuple(range(1,11))
letters = tuple("abcdefg")
print("\nPrinted tuples:")
print(nums)
print(letters)

# !!! INSTRUCTOR NOTE: peer instruction #3.1 and 3.2

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

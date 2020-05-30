# Intro to for loops notes
#   counting with the range() function 

# counting with while loops:
# CHALLENGE: Print 'Hello, world.' 10 times using a while loop
counter = 0
while counter < 10:
    print('Hello, world.')
    counter += 1

# FOR LOOP - repeats loop body FOR a certain number of times,
#            instead of based on a loop condition.

# pseudocode:
# for [loop variable] in [sequence]:                # for statement
#   repeat statements for each item in sequence     # loop body
 
# Print "Hello, world." 10 times using a for loop
input('\nPress enter to begin.')
for num in "0123456789":        # for statement
    print ('Hello, world.')     # block runs 'for each' item in sequence
 
# Display numbers 1-10 using a for loop
input("\nPress enter to begin.")
for num in "0123456789":
    print(int(num) + 1)   # num is the LOOP VARIABLE that accesses each element, one at a time

# often you will use the loop variable in the loop body, but you don't have to

print(num)  # loop variable exist outside loop! (notice the value is 9)

# range() function 
#   returns an immutable sequence of integers, of type RANGE.
#   IMMUTABLE - cannot be changed once created.
#   can accept 3 arguments: [start](optional), end(exclusive), [step](optional)
#   commonly used for looping a specific number of times with a for loop

range_of_nums = range(5) 
range_of_nums = range(1,6) 
range_of_nums = range(1,6,2) 
print("Printed range:", range_of_nums)

#   Display numbers 1-20
input("\nPress enter to begin.")
for num in range(1,21):
    print (num)   
 
# Controlling range() in more detail
#   Count 10-20, by 2's
input("\nPress enter to begin.")
nums = range(10, 21, 2) # 3rd argument in range() is the step value
for num in nums:
    print (num)
 
# Practice Challenges:
#   Increment challenge:  Count by 3’s from 3-99, inclusive
input("\nPress enter to begin.")
for n in range(3,100,3):
    print (n)

#   Counting Down Challenge: Count down by 2’s from 10 to -10, inclusive
input("\nPress enter to begin.")
for n in range(10,-11,-2):
    print (n)

# Application Challenges:

# Bug Collector Program -
#   A bug collector collects bugs every day for 7 days. Write a program that
#   keeps a running total of the number of bugs collected during the 7 days.
#   The loop should ask for the number of bugs collected for each day,
#   and when the loop is finished, the program should display the total
#   number of bugs collected. Can you get the day number to display each day?
print ("\nWelcome bug collector!\n")
bugs = 0
total = 0
for day in range(1,8):
    bugs = int(input("How many bugs did you collect on day " + str(day) + "?: "))
    total += bugs
print ("\nYou collectd a total of", total, "bugs.")
input("Press enter to exit.")
 
# Calories Burned Program-
#   Running on a treadmill you burn 3.9 calories per minute.
#   Write a program that uses a loop to display the number of
#   calories burned after 10, 15, 20, 25, and 30 minutes.
#   Display the number of minutes without hard-coding them.
print ("\nWelcome runner!\n")
for mins in range(10,31,5):
    print ("You will burn ", 3.9 * mins, "calories if you run for", mins, "minutes.")

input("Press enter to exit.")
 
# Advanced Challenge
# Pennies For Pay Program-
#   Write a program that calculates the amount of money a person would
#   earn over a period of time if their salary is one penny the first day,
#   two pennies the second day, and continues to double each day.
#   The program should ask the user for the number of days worked.
#   Display a table showing what the salary was for each day,
#   and then show the total pay at the end of the period.

days = int(input("How many days did you work?"))
salary = .01
total = 0

print("Day\tSalary")
for day in range(days):
    print(day + 1, "\t", salary)
    total += salary
    salary *= 2 
    
print("The total pay at the end of the period is", round(total, 2))
 
'''
print ("\nWelcome to the Pennies for Pay program\n")
total = 0
days = int(input("How many days have you worked?: "))
print ("\nHere is your salary by day, in pennies:\n")
print ("Day:\t\t# of pennies")
print ("Day 1\t\t 1")
for i in range(1,days):
    salary = 2**i
    print ("Day", i+1,"\t\t",salary)
    total += salary
print ("Your total pay was", total, "pennies.")
'''

input("Press enter to exit.")


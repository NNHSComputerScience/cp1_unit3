# Pizza Slicer
# Demonstrates string slicing
#  To slice, use the format [ starting index value : ending index value : step]

word = 'pizza'

# Note: A slice will always occur to the LEFT of the index value given if 
#       slicing forwards; occurs to the RIGHT if slicing backwards.

# slicing shorthand
#   we can omit values in a slice to represent the start and end of a word


print(
'''
  Slicing 'Cheat Sheets':
  
  FORWARDS:                      BACKWARDS:
 0   1   2   3   4   5              0   1   2   3   4   
 +---+---+---+---+---+          +---+---+---+---+---+ 
 | p | i | z | z | a |          | p | i | z | z | a |
 +---+---+---+---+---+          +---+---+---+---+---+
-5  -4  -3  -2  -1             -6  -5  -4  -3  -2  -1 

''')
 
# CHALLENGE: Write a program that allows the user to slice the word 'pizza'
#           as many times as they want by getting the beginning and ending 
#           index values for the slice.
word = 'pizza'

print ("Enter the beginning and ending index for your slice of 'pizza'...")
 
        
input('\n\nPress the enter key to exit.')  
































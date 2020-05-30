# intro to lists and slicing notes

# a LIST is an ordered sequence of any type, like tuples, except it is MUTABLE.
# MUTABLE - 

# creating an empty list


# list with string elements, representing two rows of cars

# looping through a list

        
# CHALLENGE: display each row of cars in a separate columns, with column headings "Row 1" and "Row 2"

    
# concatenating lists


# list mutability - lists can be modified, unlike tuples and strings


# deleting a list element
#   del keyword - del list[index_value or slice]
#   all elements to the right of the deleted element(s) get shifted left


# SLICE - targets one or more elements of a sequence.
#   To slice, use the format [ starting index value : ending index value (exclusive) : step ]
#   Note: A slice will always include the first index value specified and
#       exclude the second index value specified

word = 'pizza'

# slicing shorthand
#   we can omit values in a slice to represent the start and end of a word

# slice from index 1 to the end of the word: izza

# slice from the beginning of the word to the 2nd to last character: pizz

# slice the entire word: pizza

# this is useful for making a copy:

# the step value doesn't have to be +/- 1: pza

# IndexError: string index out of range

# invalid slice returns an empty string

print(
'''
  Slicing 'Cheat Sheet':
  
  FORWARDS:
     0   1   2   3   4   5
   +---+---+---+---+---+
   | p | i | z | z | a |
   +---+---+---+---+---+
-6  -5  -4  -3  -2  -1

''')
 
# CHALLENGE: Write a program that allows the user to slice the word 'pizza'
#           as many times as they want by inputting the beginning and ending 
#           index values for the slice.
word = 'pizza'

print ("Enter the beginning and ending index for your slice of 'pizza'...")
    
input("\nPress enter to exit.")
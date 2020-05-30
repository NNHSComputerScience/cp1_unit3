# intro to lists and slicing notes

# a LIST is an ordered sequence of any type, like tuples, except it is MUTABLE.
# MUTABLE - once creates, it can be modified.
#   e.g. [0, "a", 1.1, "hello", (1,2,3,4,5), True, 1]

# creating an empty list
row = []

# list with string elements, representing two rows of cars
row1 = ["Ford", "Audi", "BMW", "Lexus", "Honda", "Jeep"]
row2 = ["Toyota", "VW", "Buick", "Ford", "Tesla", "Nissan"]
print(row1)
print(row2)

# looping through a list
for car in row1:
    #print(car)
    if car in row2:
        print(car, "is in both rows.")
        
# CHALLENGE: display each row of cars in a separate columns, with column headings "Row 1" and "Row 2"
print("Row 1\t\tRow 2")
for i in range(len(row1)):
    print(row1[i] + "\t\t" + row2[i])
    
# concatenating lists
all_rows = row1 + row2
print(all_rows)

# list mutability - lists can be modified, unlike tuples and strings
print(row1)
row1[0] = "Hyundai"
print(row1)

first_car = row2[0]
# first_car[0] = "L"  # strings are immutable!

row1_tuple = tuple(row1)
# row1_tuple[0] = "Mercedes"  # tuples are immutable

# deleting a list element
#   del keyword - del list[index_value or slice]
#   all elements to the right of the deleted element(s) get shifted left
print(row1)
print(len(row1))
del row1[0] 
print(row1)
print(len(row1))

print(row2)
del row2[1:3]
print(row2)

# SLICE - targets one or more elements of a sequence.
#   To slice, use the format [ starting index value : ending index value (exclusive) : step ]
#   Note: A slice will always include the first index value specified and
#       exclude the second index value specified

word = 'pizza'

print(word[3 : 5]) # forward slice; prints: za

print(word[-3 : -6 : -1]) # backward slice; prints: zip

# slicing shorthand
#   we can omit values in a slice to represent the start and end of a word

# slice from index 1 to the end of the word: izza
print(word[1 : ])

# slice from the beginning of the word to the 2nd to last character: pizz
print(word[ : -1])

# slice the entire word: pizza
print(word[ : ])

# this is useful for making a copy:
word2 = word[ : ]
print(word2)

# the step value doesn't have to be +/- 1: pza
print(word[0 : : 2])

# IndexError: string index out of range
#print(word[5])

# invalid slice returns an empty string
print("**" + word[5 : 6] + "**")

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
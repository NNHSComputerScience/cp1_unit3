# Pizza Slicer
# Demonstrates string slicing
#   To slice, use the format [ starting index value : ending index value : step ]

word = 'pizza'

# Note: A slice will always occur to the LEFT of the index value given, if
#       slicing forwards; occurs to the RIGHT if slicing backwards.

print(word[3:5]) # forwards slice

print(word[-3:-6:-1]) # backwards slice

# Slicing shorthand
# we can omit values in a slice to represent the start and end of a word 

print (word[0:])     # print 0 index to end of word

print (word[:5])     # print beginning of word to index 5

print (word[:])     # print entire word.

# useful for making a copy...
word2 = word[:]
print (word2)

# can also 'step'
print(word[0::2])

# invalid index returns an error
print(word[5])
# invalid slice returns a space
print(word[5:6])

print(
"""
  Slicing 'Cheat Sheets':
  
  FORWARDS:                      BACKWARDS:
 0   1   2   3   4   5              0   1   2   3   4   
 +---+---+---+---+---+          +---+---+---+---+---+ 
 | p | i | z | z | a |          | p | i | z | z | a |
 +---+---+---+---+---+          +---+---+---+---+---+
-5  -4  -3  -2  -1             -6  -5  -4  -3  -2  -1 

""")

print ("Enter the beginning and ending index for your slice of 'pizza'.")
print ("Press Enter at 'Begin' to exit.")

begin = None    # None is Python's way of representing nothing
while begin != "":
    begin = input("\nBegin: ")

    if begin:
        begin = int(begin)
        end = int(input("End: "))

        print ("word[" , begin , ":" , end , "] is ", end=" ")
        print (word[begin:end]) # creates the slice
        
input("\n\nPress the enter key to exit.") 

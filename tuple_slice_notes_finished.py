# tuple_slice_notes_finished.py
# Indexing & slicing tuples and the .choice() function
import random

# creating tuples: The Cubs World Series game 7 lineup (in correct batting order)
#   and corresponding positions
cubs = ("Dexter Fowler",
        "Kyle Schwarber",
        "Kris Bryant",
        "Anthony Rizzo",
        "Ben Zobrist",
        "Addison Russell",
        "Willson Contreras",
        "Jason Heyward",
        "Javier Baez")
pos = ("CF", 
        "DH",
        "3B",
        "1B",
        "LF",
        "SS",
        "C",
        "RF",
        "2B")
num = ("24",
        "12",
        "17",
        "44",
        "18",
        "27",
        "40",
        "22",
        "9")
        
print(cubs) 
print(pos) 
print()

# INDEXING
#   Display 1 element: Anthony Rizzo
print(cubs[3]) 

#   Display from multiple tuples: Dexter Fowler CF
print(cubs[0] , pos[0])

# CHALLENGE #1 
#   Display all Cub outfield players using indexing
input("\nPress enter to begin CHALLENGE 1: ")
print(cubs[0] , cubs[4], cubs[7])

#   Use indexing to print a statement that says:
#   “The World Series MVP is Ben Zobrist, LF”
print("The World Series MVP is", cubs[4] + ",", pos[4]) 

# SLICING
#   Display 2 slices: 1 showing the Cubs first 3 batters and 1 showing their
#   next 6 batters
print(cubs[:3] , cubs[3:])

# CHALLENGE #2
#   Store 2 slices: the Cubs first 4 batters and their positions
#   Print the top of the lineup in a table format, including positions.
input("\nPress enter to begin CHALLENGE 2: ")
top_cubs = cubs[:4]
top_pos = pos[:4]
for i in range(len(top_cubs)):
    print(top_cubs[i] + "\t" + top_pos[i])

# Selecting a random element with .randrange()
print (cubs[random.randrange(len(cubs))])

# Selecting a random element with .choice()
print (random.choice(cubs))

# CHALLENGE #3
#   Create a 3rd tuple to hold all jersey numbers.
#   Select a random Cub using random.choice() and print info for batters in the 
#   lineup, up to and including the random batter(table format & using a for loop)
input("\nPress enter to begin CHALLENGE 3: ")

randcub = random.choice(cubs)
print("The random cub is:", randcub)
index = 0
rand_cub_index = 0
for i in cubs: 
    if i == randcub:
        rand_cub_index = index
    index += 1
print("Number \t\t Name \t\t\t Position")
for i in range(rand_cub_index+1):
    print (num[i] , "\t\t" , cubs[i] , "\t\t" , pos[i])

input("Press enter to exit.")


"""
Name: Mr. C
Title: List Methods Notes
Description: Overview of the list methods you need to know and how to use them.

METHOD - an ability or behavior of an object.

Like strings and turtles, lists are objects that have their own methods.
"""
import random
row = ["Ford", "Audi", "BMW", "Lexus", "Mercedes", "Jeep"]
print (row)

# concatenation is one way to add cars to a list, but it does not mutate the list
row += ["Ford", "Tesla"]
print(row)

# LIST METHODS mutate lists:

# 1: Append Method
#   adds an element to the end of a list
row.append("BMW")
print(row)

# we can only append one item at a time
#row.append("Toyota", "Ford") 
# ERROR: TypeError: append() takes exactly one argument (2 given)

# 2: Pop method
#   removes an element by index value from a list and returns it
#   try to... remove the first car in the row
car1 = row.pop(0)
car2 = row.pop(0)
print(row)
print("Returned cars:", car1, car2)


# 3: Remove method
#   removes the first occurence of an element from a list
#   try to... remove the BMW
row.remove("BMW")
print(row)
row.remove("BMW")
print(row)
 
# 4: Sort method
#   sorts a list in ascending order
#	strings sort alphabetically, numbers numerically
#   try to... sort the list in ascending order
row.sort()
print(row)

# 5: Reverse method
#   reverses the order of a list
#   try to... sort the list in descending order
row.reverse()
print(row)

# 6: Count method
#   counts the number of occurances of an element
#   try to... count the number of "Ford" cars in the row
row.append("Ford")
row.append("Ford")
print(row)
num_fords = row.count("Ford")
print("Number of Fords:", num_fords)
print(row)

# 7: Index method
#   displays the index value of an element
#   try to... display the index value of the "Jeep"
jeep_index = row.index("Jeep")
print("Jeep index is:", jeep_index)

# 8: Insert method
#   inserts an element at a specific index value
#   try to... insert a "Harley Davidson" in the second parking spot
print(row)
row.insert(1, "Harley Davidson")
print(row)

# random.choice(sequence) function
#	Return a random element from a sequence, as long as there are items left in the sequence.

rand_car = random.choice(row)
print("A random car:", rand_car)
print("A random vowel:", random.choice("AEIOU"))

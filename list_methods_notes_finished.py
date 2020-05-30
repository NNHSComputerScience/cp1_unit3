# List Methods Notes
# METHOD - an ability or behavior that an object has; something it can do.
#   Like strings and turtles, lists are objects that have their own behavior, 
#     or list methods.

row = ["Ford", "Audi", "BMW", "Lexus", "Mercedes", "Jeep"]
print(row)

row += ["Ford", "Tesla"] # concatenation is one way to add item(s) to a list, but it doesn't mutate the list

# LIST METHODS mutate the list

# 1: Append Method
#   adds an element to the end of a list
row.append("Ford")
print(row)

#append multiple is a trap!
#row.append("Ford", "Buick")
#print(row) 

car = 1
while car:
    car = input("Enter a car to add (leave blank to exit): ").title()
    if car:
        row.append(car)

# 2: Pop method
#   removes an element by index value from a list and returns it
row.pop(0)
print(row)

# 3: Remove method
#   removes an element from a list (a value)
#   del/pop removes an index value
row.remove("BMW")
print(row)

# this method removes the first occurance of an element only
row.remove("Ford")
print(row)

# 4: Sort method
#   sorts a list in ascending order
row.sort()
print(row)

# 5: Reverse method
#   reverses the order of a list
row.reverse()
print(row)
row.reverse()
print(row)

# 6: Count method
#   counts the number of occurances of an element
print(row.count("Ford"))

# 7: Index method
#   displays the index value of an element
print(row.index("Lexus"))

# 8: Insert method
#   inserts an element at a specific index value
row.insert(2, "Kia")
print(row)

input("Press enter to exit.")

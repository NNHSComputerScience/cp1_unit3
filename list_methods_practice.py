# list methods practice activity
import random

# PART 1
items = []
prices = []

item = input("First item (leave blank to stop): ").lower()
while item:
   price = float(input("Price: "))
   items.append(item)
   prices.append(price)
   item = input("Next item (leave blank to stop): ").lower()

# PART 2
print("\nItems:\t\tPrices:")  	# table header
for i in range(len(prices)):  	# loop through range of indices
	print("{}\t\t${:.2f}".format(items[i], prices[i]))

# PART 3
rand_item = random.choice(items) 
rand_index = items.index(rand_item)
prices[rand_index] = prices[rand_index] * .5

# alternate way
'''
index_count = 0
for i in items:
   if rand_item == i:  		    # find the random item
      rand_index = index_count  # save the random item’s index
      # or, rand_index = items.index(rand_item)
      prices[rand_index] = prices[rand_index] * .5 # update price
   index_count += 1
'''

print("\nFLASH SALE! A random item has been discounted by 50%:  Your {} is now ${:.2f}.".format(items[rand_index], prices[rand_index]))

# PART 4
print("\n", items) 
index_count = 0
for i in range(len(items)):
    if "eggs" == items[i]:  		  # find the eggs
        removed = items.pop(i)		  # remove eggs
        prices.pop(i)					  # remove eggs price

print("The", removed, "have been removed.")
print(items)

# alternate way
#eggs_index = items.index(“eggs”)
#items.pop(eggs_index)
#prices.pop(eggs_index)


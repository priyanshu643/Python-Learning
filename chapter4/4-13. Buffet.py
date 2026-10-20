"""A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.

•Use a for loop to print each food the restaurant offers.

•Try to modify one of the items, and make sure that Python rejects the
change.

•The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu."""
# add a tuple with a variable assigned
foods = ('shai pneer', 'mix veg', 'tandoori roti', 'gulab jamun', 'dal makhani')

print('----' * 10)  # decoration
# adding a for loop to print the all the food items in the tuple foods
for food in foods:
    print(food.title()) # printing the food items
print('----' * 10 + '\n') # decoration


# trying to modify the one of the item in the tuple foods and assuring that this returns an error
# foods.append('cham cham')

# writing over the tuple foods
foods = ('shai paneer', 'mix veg', 'tandoori roti', 'cham cham', 'dal tadka')
# adding a for loop to print all the food items separately

print('----' * 10)  # decoration
for food in foods:
    print(food.title()) # printing the food items
print('----' * 10 + '\n') # decoration

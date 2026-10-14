"""Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

•Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.

•Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.

•Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list."""

# adding the list
animals = ['cat', 'dog', 'rat', 'hamster']

print('----' * 10) # decoration
# adding the for loop to print the first 3 items.
for animal in animals[:3]:
    print(f"The first three items in the list are: {animal}") # printing a message for all the first three animals.
print('----' * 10) # decoration

print('----' * 10) # decoration
# adding a list for middel elements.
for animal in animals[1:4]:
    print(f"Three items from the middle of the list are: {animal}") # printing a message for all the middel animals.
print('----' * 10) # decoration

print('----' * 10) # decoration
# adding a for loop to print from last
for animal in animals[-3:]:
    print(f"The last three items in the list are: {animal}") # printing the last animal names with a message
print('----' * 10) # decoration
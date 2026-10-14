"""Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.

•Modify your program to print a statement about each animal, such as A
dog would make a great pet.

•Add a line at the end of your program, stating what these animals have in
common. You could print a sentence, such as Any of these animals would
make a great pet!"""

# adding the animals to the list
animals = ['cat', 'dog', 'rat', 'hamster']
# using a for loop to print the name of animals individually.

for animal in animals:
    # print(animal) # printing the animals name separately.
    # now printing all the animals name with a message
    print('----' * 10)  # decoration
    print(f"{animal.title()} is great to have a pet.")
    print(f"{animal.title()}, wood be a great pet.")
    print('----' * 10)  # decoration
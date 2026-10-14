"""Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
•Add a new pizza to the original list.
•Add a different pizza to the list friend_pizzas.
•Prove that you have two separate lists. Print the message My favorite piz-
zas are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list."""

# adding the pizza lists.
pizzas =  ['margarita', 'Chez burst', 'Peppy Paneer']
# copying the pizzas to friend_pizzas
friend_pizzas = pizzas[:]
# adding the corn pizza to the pizzas list.
pizzas.append('corn')
# adding the pizza to the friend_pizzas list
friend_pizzas.append('onion')
# adding the for loop to print the list of fav pizzas of mine
for pizza in pizzas:
    print(f"My fav pizzas are: {pizza} Pizza") # printing the pizzas with the message
# adding the for loop to print the list of fav pizzas of my friend
for friend_pizza in friend_pizzas:
    print(f"My friend's fav pizzas are: {friend_pizza} Pizza") # printing friend's fav pizza with a message
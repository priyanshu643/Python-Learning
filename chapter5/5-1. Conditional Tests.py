"""Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False."""

# making a list of cas with a variable cars
cars = ['BMW', 'AUDI', 'Ferrari']

# adding a loop in the statement to just check it with if block.
for car in cars:
    # if statements to check that does those cars even exists in the list or not
    if car == 'BMW':
        print(True) # now print the statement
    if car == 'AUDI':
        print(True) # now print the statement
    if car == 'Ferrari':
        print(True) # now print the statement
print('----' * 10) # decoration
# Creating 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False
# making list of 5 names of pizza in to Dominos menu
pizzas = ['Margherita', 'Farmhouse', 'Mexican Green Wave', 'Indi Tandoori Paneer', 'Chicken Dominator']

# adding a for loop to get all items inside the list separately
for pizza in pizzas:
    # if statements to get 5 True and 5 False
    if pizza == 'Chicken Dominator':
        print("True") # printing the result
    elif pizza == 'Indi Tandoori Paneer':
        print("True")  # printing the result
    elif pizza == 'Mexican Green Wave':
        print("True")  # printing the result
    elif pizza == 'Farmhouse':
        print("True")  # printing the result
    elif pizza == 'Margherita':
        print("True")  # printing the result
    elif pizza == 'Double Cheese Margherita':
        print("True")  # printing the result
    elif pizza == 'Peppy Paneer':
        print("True")  # printing the result
    elif pizza == 'Veg Extravaganza':
        print("True")  # printing the result
    elif pizza == 'Cheese n Corn':
        print("True")  # printing the result
    elif pizza == 'Pepper Barbecue Chicken':
        print("True")  # printing the result
    else:
        print("False")
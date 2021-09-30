# Conditional (if) statements - used to run code only if a condition and/or set of conditions is true

# Handy reference for if/elif/else statements, thanks to Mel:
# https://www.w3resource.com/python/python-if-else-statements.php

name = "Random name"
if name == "Adrian" or name == "Mel":
    print("I recognize that name!")
else:
    print("Hmm - I don't know that name")

# More practice - play around with the num variable!
num = 30
if num < 10:
    print("I'm less than 10")
elif num >= 10 and num <= 20:
    print("I'm between 10 and 20")
else:
    print("I'm bigger than 20")

"""
Defining a for loop:
A for loop is used when you want to run the same code a bunch of times.  It's used a lot to loop through lists, dictionaries,
tuples, and combinations of these.  The syntax is usually:

for var_name in collection_to_examine:
    # Run code here

OR
for var_name in range(values):
    # Run code here

Not shown in lecture, but handy to remember: a while loop
A while loop is used if you want to run code, but you don't know how many times beforehand you'll need to run the code.
IMPORTANT: make sure the variable(s) you are checking for your while loop are incremented somehow, otherwise you'll 
find yourself in an infinite loop.
"""
# Range statement in loops
for j in range(10): # Start at 0 (default), end at 9 - the last value before 10, step size = 1 (default); number of times to run loop
    print(j)

for k in range(5,11): # Start at 5, end at 10 (last valid number before 11), step size = 1 (default)
    print(k)

for q in range(5,18,2): # Start at 5, end at 17 (last valid number before 18), step size = 2
    print(q)

"""
Functions:
Functions are similar to for loops in that you can run the same code a bunch of times - basically to eliminate redundancy.
However, functions allow you to pass in values.  Think of a function as like a recipe - you're writing a set of instructions
(code) that will run the same way regardless of the input(s).
"""

# Loop through a list of values
# METHOD 1: using the range and len functions:
def sum_list(list):
    sum = 0 # Variable will start our sum off
    # For loop to go through the list
    for i in range(len(list)): # Loop through the indices
        sum += list[i]
    return sum

my_list = [3, 8, 4, 1, 9, 7, 3]
print(sum_list(my_list))

# METHOD 2: Loop through the values themselves without using indices
def sum_list_v2(list):
    sum = 0 # Variable will start our sum off
    # For loop to go through the list
    for val in list:
        # print(val)
        sum += val
    return sum

this_sum = sum_list_v2(my_list)
print(this_sum)

# Demonstration of a nested for loop with a list of lists

# Defining a list of lists, where a bigger list contains entries where each item is another list
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(grid)

# Couple of ways to loop through all the items

for i in range(len(grid)): # could call i as "row"
    print(grid[i])
    for j in range(len(grid[i])): # could call j as "col"
        print(grid[i][j])

for i in range(len(grid)):
    row = grid[i]
    print(row)
    for j in range(len(row)):
        print(row[j])

"""
Optional parameters
Whenever you define a function, you can use optional parameters by giving those variables default values.  So when a function
is called, and no value is passed in for that parameter, a default value will be used.

NOTE: ALL optional parameters must come AFTER required parameters (see countdownV3 for an example).
"""
def countdown(start = 10):
    for k in range(start,0,-1):
        print(k)
    print("Liftoff!")

countdown()
countdown(5)

def countdownV2(start = 10, end = 0):
    for k in range(start,end,-1):
        print(k)
    print("Liftoff!")

countdownV2()
countdownV2(5)

def countdownV3(start, end = 0):
    for k in range(start,end,-1):
        print(k)
    print("Liftoff!")

countdownV3(8)

"""
Break and continue statements
Sometimes you'll want to exit a loop early.  If you want to do just that, use a "break" statement.
If you want to go straight to the next iteration of a loop without leaving necessarily, use a "continue" statement.

"""
# Break statement
for n in range(10):
    print(n)
    if n > 5:
        break


# Continue statement
# Print all values from 0 through 9 EXCEPT 5
for n in range(10):
    if n == 5:
        continue
    else:
        print(n)

"""
Loop through a list of dictionaries

"""
some_users = [
    {
        'first_name': 'Adrian',
        'number': 1,
        'color': 'blue',
    },
    {
        'first_name': 'John',
        'number': 2,
        'color': 'red',
    },
    {
        'first_name': 'Jane',
        'number': 3,
        'color': 'green',
    }
]

# Print the first names of everybody
for i in range(len(some_users)): # Loop through the list
    print(some_users[i].get("first_name")) # Method 1 with the .get method
    print(some_users[i]["first_name"]) # Method 2

# Loop through the keys and values
for i in range(len(some_users)): # Loop through the list
    # Method 1: with .items():
    for this_key, this_val in some_users[i].items():
        print(f"{this_key}: {this_val}")

    # Method 2: with .keys():
    # for key in some_users[i].keys():
    #     print(f"{key}: {some_users[i][key]}")
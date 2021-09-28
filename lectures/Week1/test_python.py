x = 10 # NOTE: do NOT use semicolons!!
y = True # or False - notice the capitalization!!!
z = "Hello world!" # String

# Handy extension: indent-rainbow for showing
def test_function(): # Defining a function - don't forget the colon at the end!
    m = 10 # Note the indentation here
z2 = 20 # But not here!

print(z2)

some_string = 'Another string'

# Two ways to concatenate a string - one adds a space, and one doesn't
# print(some_string + 'again')
# print(some_string,"again")

print(some_string,x)
# # print(some_string+x) # Will produce an error
print(some_string,str(x)) # Use the str command to turn a number into a string

print(f"My favorite number is {x}.")

# Lists
some_list = [10, True, "Hi", [3,8,4]]
some_list.append(3.5)
print(some_list)
print(len(some_list))
print(some_list[3])
print(some_list[4])
print(type(some_list))

# Tuples
my_tuple = (5, -3, 8, 4)
# my_tuple.append(10) # ERROR - cannot add or remove values - a tuple's values stay fixed
# my_tuple[2] = 12 # ERROR - cannot change values

# Slicing - a way to retrieve values between indices (indexes)
print(some_list)
print(some_list[1:]) # Print values from index 1 to the end - including the end
print(some_list[:3]) # Values from 0 through index 2, but EXCLUDING index 3
print(some_list[1:3]) # Values at indices 1 and 2
print(some_list[::2]) # [starting index]:[ending index that's EXCLUDED]:increment - in this example, index 0, 2, 4, ...

# Dictionaries

my_dictionary = {
    "number": 20, # "key-value" pairs
    "favorite_word": "Hello",
}
print(my_dictionary["number"]) # Access a value
my_dictionary["favorite_food"] = "pizza"
print(my_dictionary) # Print dictionary with key-value pair

# Two ways to remove a key-value pair - the .pop() method or using the "del" keyword
my_dictionary.pop("number") 
# print(my_dictionary)
del my_dictionary["favorite_food"]
# print(my_dictionary)


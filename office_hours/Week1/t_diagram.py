#6
def add(b,c):
    # print(b+c)
    return b + c
# print(add(1,2) + add(2,3))
# If a function doesn't have a return statement, it will return the value None (Python keyword)

# [4, 3, 8, 11, 2, 7]
# Minimum value of a list
def findMin(lst):
    min = lst[0] # Start with the first value in the list to get us started
    for i in range(1,len(lst)): # We start off at index 1 because we already took the value from index 0
        if lst[i] < min:
            min = lst[i] # Set the new minimum value
    # print(min)
    return min

# print(findMin([4,3,8,11,2,7]))

def findMin2(lst):
    min = lst[0]
    for value in lst[1:]: # Use slicing to start at index 1 (the second value)
        print(value)
        if value < min:
            min = value # Set the new minimum value
    # print(min)
    return min

print(findMin2([4,3,8,11,2,7]))

def countdown(num1):
    for x in range(num1,0,-1):
        print(x)
countdown(5) # No need for a print here since we're not returning a value from the function (i.e. no return statement)


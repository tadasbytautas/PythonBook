# Beginner Exercises
#
# Hello World!
# Output “Hello World!” to the console.
def hello_world():
    return "Hello World!"


# Assignment
# Store “Hello World!” in a variable, then output it to the console.
def storeHello():
    hello = "Hello World!"
    return hello


# Parameters
# Create a method that gets a string from the user, and then outputs that string to the console.
def newString():
    new = str(input("new string: "))
    return new


# Parameters/Operators
# Create a method that accepts two integers as an input, then returns an integer that is a sum of the two integers given.
def sumOfInts(input1, input2):
    int1 = int(input1)
    int2 = int(input2)
    return int1 + int2


# Conditionals
# Modify your method from the Parameters/Operators task to accept another parameter, a Boolean, which if it is true,
# the method will print a sum of the two numbers, and if it is false it will print the multiplication of the two numbers.
def conditionals(input_1, input_2, user_bool):
    int1 = int(input_1)
    int2 = int(input_2)
    con = user_bool
    if con:
        return int1 + int2
    elif not con:
        return int1 * int2


# Conditionals 2
# Modify your method from the Conditionals task to have another if statement that checks if one of the numbers is 0,
# if this is true then print the other non-0 number.
# Input -> 1, 0 Return 1
# Input -> 1, 2 Return 3
def conditionals_two(input_1, input_2, user_bool):
    int1 = int(input_1)
    int2 = int(input_2)
    con = user_bool

    if int1 == 0:
        return int2
    elif int2 == 0:
        return int1
    else:
        pass

    if con:
        return int1 + int2
    elif not con:
        return int1 * int2


# Recursion
# Create a for loop that will call and output the result of your method from the
# Conditionals 2 task 10 times.

def recursion(input_1, input_2, user_bool):
    new_list = ""
    for i in range(10):
        new_list =+ conditionals_two(input_1, input_2, user_bool)
    return new_list

# Lists
# Create a list with 10 integer values in it, then call and output the first element in the list.
def newList(num):
    l = []
    for i in range(10):
        l =+ int(num)
    return l

# Recursion/Lists
# Using your list that you created in the Lists task, create a loop that iterates through your list, outputting the values contained within it.

# Recursion/Lists
# Create a loop that populates a list with values, outputting them at each iteration. Then create another loop that iterates through the array, changing the values at each point to equal itself times 10, outputting them at each iteration.
# Example Output
# 1,2,3,4…
# 10,20,30,40…

# User input
# Modify the previous task to take input from the user, taking an integer off of the user and using that integer to determine how large the array is going to be.

# Functions
# Create a function that asks the user for a number and whether they want to double or triple the number. Have methods within the function for doubling and tripling the user’s number.

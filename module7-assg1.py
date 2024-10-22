# Assignment 1.

# Create a program that accepts a list of 5 integers as input
# and rearranges it by swapping the first and last numbers.
# Employ a loop to input these integers into the list,
# then display the updated list as a whole. (See example below)

# Sample console:

# >>Enter a string of numbers. 2

# >>Enter a string of numbers. 4

# >>Enter a string of numbers. 6

# >>Enter a string of numbers. 8

# >>Enter a string of numbers. 10

# >>The first and last numbers swapped is: [10, 4, 6, 8, 2]

# Assignment 1.

# Create an empty list to store the integers entered by the user.
list = []

# Prompt the user to enter the first number and immediately append it to the list.
list.append(int(input("Enter a number: ")))

# Use a for loop to input the next 4 numbers. 
# The range is from 0 to 4, but since the first number is already inputted, 
# this will prompt the user four more times, making a total of 5 integers in the list.
for i in range(0, 4):
    list.append(int(input("Enter another number: ")))

# The first and last numbers need to be swapped. 
# Start by appending the first element (at index 0) to the end of the list.
list.append(list[0])

# Insert the last but one element (second to last, which is the original last number) 
# at the beginning of the list, so it becomes the new first element.
list.insert(0, list[len(list) - 2])

# Remove the second element (which is the original first number) 
# from its original position, since it's now duplicated.
list.pop(1)

# Remove the second to last element, which is the original last number 
# that has now been moved to the front of the list.
list.pop(len(list) - 2)

# Output the final result to the user with the swapped first and last numbers.
print(f'The first and last numbers swapped is: {list}')

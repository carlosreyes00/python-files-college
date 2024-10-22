# Prompt the user to input a list of numbers separated by commas.
input_numbers = input("Enter a list of numbers separated by commas: ")

# Split the input string into a list of numbers (as strings), then convert them to integers.
numbers = [int(num.strip()) for num in input_numbers.split(',')]

# Calculate the total sum of the numbers.
total = sum(numbers)

# Calculate the average of the numbers.
average = total / len(numbers)

# Identify the largest number in the list.
largest = max(numbers)

# Identify the smallest number in the list.
smallest = min(numbers)

# Display the total, average, largest, and smallest numbers.
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

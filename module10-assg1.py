entry = int(input("Entry the upper limit: "))

def sum_odd_integers(n):
    # Base case: if n is less than or equal to 0, return 0
    if n <= 0:
        return 0
    # If n is odd, include it in the sum, and make a recursive call with (n - 2)
    elif n % 2 != 0:
        return n + sum_odd_integers(n - 2)
    else:
        # If n is even, skip it and call the function with (n - 1)
        return sum_odd_integers(n - 1)

# Example usage
result = sum_odd_integers(entry)
print("Sum of odd integers up to 9 is:", result)
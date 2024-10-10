# Develop a program that takes input values in USD dollars,
# and converts them into three different currencies:
# Pound Sterling, Japanese Yen, and Canadian Dollar.
# The program should include three distinct functions named
# pound_conversion,
# japanese_conversion,
# and canadian_conversion,
# all of which should be called within the main part of the code and return the appropriate exchange amounts.
# Conversion rates are provided below:

# $1.00 USD --> $0.77 Pound Sterling
# $1.00 USD --> $157.50 Japanese Yen
# $1.00 USD --> $1.37 Canadian Dollar
# (Values are based as of August 2024)

def pound_conversion(usd):
    return usd * 0.77

def japanese_conversion(usd):
    return usd * 157.5

def canadian_conversion(usd):
    return usd * 1.37

amount = float(input("\nEnter how much money (USD) you want to change -> "))

print(f"${amount:.2f} is:\n")
print(f"{pound_conversion(amount):.2f} Pound Sterling")
print(f"{japanese_conversion(amount):.2f} Japanese Yen")
print(f"{canadian_conversion(amount):.2f} Canadian Dollar")
# Children under 5 years old: Admission is complimentary (Free of charge).
# Children aged 5 to 18 years old: A ticket costs $20.
# Adults aged 18 years and older: Tickets are priced at $60.
# Seniors aged 55 years and older: Special pricing applies, with tickets priced at $50.

print("\nWelcome to Python Park🐍")
age = int(input("Insert your age: "))
price = 0

if age < 5:
    price = 0
elif age < 18:
    price = 20
elif age >= 18 and age < 55:
    price = 60
else:
    price = 50

print(f'Your ticket cost is ${price}. Enjoy!')
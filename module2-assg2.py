gas_price = float(input("How much is the gas per gallon? -> "))

mpg = 0
while mpg == 0:
    mpg = float(input("What is your car's miles per gallon? -> "))
    if mpg == 0:
        print("MPG can't be zero, try again please")

distance = float(input("How many miles will you travel? -> "))

cost_per_mile = gas_price / mpg

print(f'Total cost:{cost_per_mile * distance: .2f}')
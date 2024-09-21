num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second one: "))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')

if num2 != 0:
    print(f'{num1} / {num2} = {num1 / num2}')
else:
    print("division by 0 is undefined")
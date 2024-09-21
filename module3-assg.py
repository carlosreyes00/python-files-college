print('\nWELCOME TO THE PASSWORD GENERATOR')

password = ""

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

digits = input("Enter a three-digit integer: ")

if len(last_name) >= 4:
    password += last_name[0:4]
else:
    password += last_name

if len(first_name) >= 3:
    password += first_name[0:3]
else:
    password += first_name

password += "."

password += digits[1]
     
print(f'\nYour password is {password}')
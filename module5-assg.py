# Your program should specify the nature of invalid credit score entries,
# indicating whether they are too high or too low. For example, if a score of 399 is entered,
# the program should indicate that it is too low; if 900 is entered, it should indicate that it is too high.
# (See sample output for more details)

# >>What is your credit score? 890
# >>Invalid credit score. This score is too high. Please enter a valid credit score. 730

# >>What is your debt amount? -1
# >>Your debt amount cannot be less than 0. Please enter a valid debt amount. 100

# >>What is your salary? -20
# >>Your salary cannot be negative. Please enter a valid salary. 70000

credit_score = int(input("What is your credit score? -> "))
credit_score_needs_reenter = credit_score < 400 or credit_score > 850
while credit_score_needs_reenter:
    if credit_score < 400:
        credit_score = int(input("Invalid credit score (too low). Try again -> "))
    else:
        credit_score = int(input("Invalid credit score (too high). Try again -> "))
    credit_score_needs_reenter = credit_score < 400 or credit_score > 850

debt_amount = int(input("What is your debt amount? -> "))
debt_amount_needs_reenter = debt_amount < 0
while debt_amount_needs_reenter:
    debt_amount = int(input("Debt amount cannot be less than 0. Try again -> "))
    debt_amount_needs_reenter = debt_amount < 0

annual_salary = int(input("What is your salary? "))
annual_salary_needs_reenter = annual_salary < 0
while annual_salary_needs_reenter:
    annual_salary = int(input("Debt amount cannot be less than 0. Try again -> "))
    annual_salary_needs_reenter = annual_salary < 0

# conditions to get mortgage
credit_score_to_get_mortgage = credit_score > 720
debt_amount_to_get_mortgage = debt_amount <= 1000
annual_salary_to_get_mortgage = annual_salary >= 60000
getting_mortgage = credit_score_to_get_mortgage and debt_amount_to_get_mortgage and annual_salary_to_get_mortgage

if getting_mortgage:
    print("Congrats, you qualify for a mortgage!")
else:
    print("Based on this information, you do not qualify for a mortgage.")
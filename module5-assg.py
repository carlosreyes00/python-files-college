credit_score = int(input("\nWhat is your credit score? -> "))
while credit_score < 400 or credit_score > 850:
    if credit_score < 400:
        credit_score = int(input("Invalid credit score (too low). Try again -> "))
    else:
        credit_score = int(input("Invalid credit score (too high). Try again -> "))

debt_amount = int(input("What is your debt amount? -> "))
while debt_amount < 0:
    debt_amount = int(input("Debt amount cannot be less than 0. Try again -> "))

annual_salary = int(input("What is your salary? "))
while annual_salary < 0:
    annual_salary = int(input("Annual salary cannot be negative. Try again -> "))

# conditions to get mortgage
credit_score_to_get_mortgage = credit_score > 720
debt_amount_to_get_mortgage = debt_amount <= 1000
annual_salary_to_get_mortgage = annual_salary >= 60000
getting_mortgage = credit_score_to_get_mortgage and debt_amount_to_get_mortgage and annual_salary_to_get_mortgage

if getting_mortgage:
    print("Congrats, you qualify for a mortgage!")
else:
    reasons = ""
    if not credit_score_to_get_mortgage:
        reasons += "\n- Credit score is lower than required"
    if not debt_amount_to_get_mortgage:
        reasons += "\n- Debt amount is higher than required"
    if not annual_salary_to_get_mortgage:
        reasons += "\n- Annual salary is lower than required"
    print("\nYou do not qualify for a mortgage due to the following reason(s):" + reasons)
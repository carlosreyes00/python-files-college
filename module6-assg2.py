# Create a program that uses a function to calculate the gross pay for full-time employees in an organization. 
# The program should first prompt users to enter their hourly rate and the number of hours worked.
# A function should then be defined to accept two parameters: the hourly rate and the hours worked, with a default value of 40 hours representing a standard workweek. The function should compute the gross pay, where the base pay for regular hours is the hourly rate, and any hours worked beyond 40 hours are paid at a 1.5x rate of the regular hourly pay; it should then return the total gross pay when called within the main program.

hourly_rate = float(input("\nEnter your hourly rate -> "))
hours_worked = float(input("Enter the number of hours worked -> "))

def gross_pay(hourly_rate, hours_worked=40):
    pay = hourly_rate * min(40, hours_worked)

    if hours_worked > 40:
        pay += (hours_worked - 40) * hourly_rate * 1.5
        return pay
    
    return pay

print(f"Your gross pay is ${gross_pay(hourly_rate,hours_worked):.2f}")
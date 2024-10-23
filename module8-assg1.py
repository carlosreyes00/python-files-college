# Create a class named BankSystem that simulates basic banking operations.
# The class should have two attributes: customer_name and starting_balance,
# which are set when the class is instantiated.

# Your class should include functions that are able to:

# Calculate Deposits: Adds a specified amount to the customer's balance.
# Process Withdrawals: Deduct a specified amount from the customer's balance. 
# If the withdrawal amount exceeds the current balance,
# display a message indicating that the transaction cannot be completed.
# Ensure that NO funds are withdrawn if the balance would drop below zero.
# Display Customer Information: Returns the customer’s name and current balance.
# These items should be returned/printed from the function. After implementing the class,

# write code to:
# Create two BankSystem objects with different customer names and starting balances.
# Perform a deposit operation on one object and a withdrawal operation on the other.
# Display the Customer Information for both objects to show their final balances.
# Sample Console: 

# (Based on an Object with a name of Devin and a starting value of $1,000. )

# >>What is your deposit amount? 200
# >>1200
# >>What is your withdrawal amount? 1300
# >>Insufficient Funds. 
# >>Hello Devin. Your current Balance is $1,200. 

class BankSystem:
    def __init__(self, customer_name, starting_balance):
        self.customer_name = customer_name
        self.starting_balance = starting_balance

    def add_deposit(self, amount):
        if amount > 0:
            self.starting_balance += amount
            print(f"The new balance for {self.customer_name} is ${self.starting_balance:.2f}")
        else:
            print("You can't deposit a non-positive amount of money") 

    def withdraw_money(self, amount):
        if amount > 0:
            if amount <= self.starting_balance:
                self.starting_balance -= amount
                print(f"The new balance for {self.customer_name} is ${self.starting_balance:.2f}")
            else:
                print("Insufficient Funds")
        else:
            print("You can't withdraw a non-positive amount of money") 

    def get_info(self):
        print(f'{self.customer_name} has ${self.starting_balance:.2f} in the bank account.')

print("\nWelcome to Python's Bank System\n")

name1 = input("Input the name of the first person => ")
initial_balance1 = float(input(f"Input the starting balance for {name1} => "))

name2 = input("Input the name of the second person => ")
initial_balance2 = float(input(f"Input the starting balance for {name2} => "))

client1 = BankSystem(name1, initial_balance1)
client2 = BankSystem(name2, initial_balance2)

client1.get_info()
client2.get_info()

deposit_amount_for_client1 = float(input(f"\nInput your deposit amount for {client1.customer_name} => "))
client1.add_deposit(deposit_amount_for_client1)

withdraw_amount_for_client2 = float(input(f"\nInput your withdraw amount for {client2.customer_name} => "))
client2.withdraw_money(withdraw_amount_for_client2)

print("")
client1.get_info()
client2.get_info()
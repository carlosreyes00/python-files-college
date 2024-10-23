# Define the BankSystem class
class BankSystem:
    # Constructor to initialize the customer name and starting balance
    def __init__(self, customer_name, starting_balance):
        self.customer_name = customer_name  # Assign customer name
        self.starting_balance = starting_balance  # Assign starting balance

    # Method to add a deposit to the balance
    def add_deposit(self, amount):
        if amount > 0:  # Ensure deposit amount is positive
            self.starting_balance += amount  # Add deposit to balance
            print(f"The new balance for {self.customer_name} is ${self.starting_balance:.2f}")
        else:
            print("You can't deposit a non-positive amount of money")  # Handle invalid deposit amount

    # Method to process a withdrawal
    def withdraw_money(self, amount):
        if amount > 0:  # Ensure withdrawal amount is positive
            if amount <= self.starting_balance:  # Check if there are sufficient funds
                self.starting_balance -= amount  # Deduct withdrawal from balance
                print(f"The new balance for {self.customer_name} is ${self.starting_balance:.2f}")
            else:
                print("Insufficient Funds")  # Handle insufficient funds
        else:
            print("You can't withdraw a non-positive amount of money")  # Handle invalid withdrawal amount

    # Method to display customer information
    def get_info(self):
        print(f'{self.customer_name} has ${self.starting_balance:.2f} in the bank account.')

# Welcome message
print("\nWelcome to Python's Bank System\n")

# Gather input for the first customer
name1 = input("Input the name of the first person => ")
initial_balance1 = float(input(f"Input the starting balance for {name1} => "))

# Gather input for the second customer
name2 = input("Input the name of the second person => ")
initial_balance2 = float(input(f"Input the starting balance for {name2} => "))

# Create two BankSystem objects with different customer names and starting balances
client1 = BankSystem(name1, initial_balance1)
client2 = BankSystem(name2, initial_balance2)

# Display the initial balance information for both clients
client1.get_info()
client2.get_info()

# Process a deposit for the first client
deposit_amount_for_client1 = float(input(f"\nInput your deposit amount for {client1.customer_name} => "))
client1.add_deposit(deposit_amount_for_client1)

# Process a withdrawal for the second client
withdraw_amount_for_client2 = float(input(f"\nInput your withdraw amount for {client2.customer_name} => "))
client2.withdraw_money(withdraw_amount_for_client2)

# Display the final balance information for both clients
print("")
client1.get_info()
client2.get_info()
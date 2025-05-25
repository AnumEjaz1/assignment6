class Bank:
    # Class variable
    bank_name = "National Bank"

    # Class method to change bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Create instances of Bank
customer1 = Bank()
customer2 = Bank()

# Print bank_name from both instances (before change)
print("Before change:")
print("Customer 1 Bank:", customer1.bank_name)
print("Customer 2 Bank:", customer2.bank_name)

# Change the bank name using class method
Bank.change_bank_name("United Bank")

# Print bank_name from both instances (after change)
print("\nAfter change:")
print("Customer 1 Bank:", customer1.bank_name)
print("Customer 2 Bank:", customer2.bank_name)

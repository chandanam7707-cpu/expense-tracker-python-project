income = float(input("Enter your monthly income: "))

expense_name = input("Enter expense name: ")
expense_amount = float(input("Enter expense amount: "))

balance = income - expense_amount

print("\n----- EXPENSE SUMMARY -----")
print("Income:", income)
print("Expense:", expense_name)
print("Amount:", expense_amount)
print("Remaining Balance:", balance)
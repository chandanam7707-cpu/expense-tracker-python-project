expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n----- ALL EXPENSES -----")

        for expense in expenses:
            print(expense["name"], ": ₹", expense["amount"])


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense: ₹", total)


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
import csv

FILE_NAME = "expenses.csv"


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount"])

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "amount": amount
        })

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\n----- ALL EXPENSES -----")

            total = 0

            for expense in reader:
                name = expense["name"]
                amount = float(expense["amount"])

                print(name, ": ₹", amount)

                total = total + amount

            print("------------------------")
            print("Total Expense: ₹", total)

    except FileNotFoundError:
        print("No expenses found.")


def delete_expense():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

        if len(expenses) == 0:
            print("No expenses found.")
            return

        print("\n----- EXPENSES -----")

        for i, expense in enumerate(expenses, start=1):
            print(i, ".", expense["name"], ": ₹", expense["amount"])

        choice = int(input("Enter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(choice - 1)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "amount"]
            )

            writer.writeheader()
            writer.writerows(expenses)

        print(deleted["name"], "deleted successfully!")

    except FileNotFoundError:
        print("No expenses found.")

    except ValueError:
        print("Please enter a valid number.")


def total_expense():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            total = 0

            for expense in reader:
                total = total + float(expense["amount"])

            print("Total Expense: ₹", total)

    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        total_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
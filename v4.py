import csv
import pandas as pd
import numpy as np
from datetime import date

FILE_NAME = "expenses.csv"


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter expense amount: "))

    expense_date = date.today().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "category", "amount", "date"]
        )

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "category": category,
            "amount": amount,
            "date": expense_date
        })

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\n----- ALL EXPENSES -----")

            for expense in reader:
                print(
                    expense["name"],
                    "|",
                    expense["category"],
                    "| ₹",
                    expense["amount"],
                    "|",
                    expense["date"]
                )

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
            print(
                i, ".",
                expense["name"],
                "|",
                expense["category"],
                "| ₹",
                expense["amount"],
                "|",
                expense["date"]
            )

        choice = int(input("Enter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(choice - 1)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "category", "amount", "date"]
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
        data = pd.read_csv(FILE_NAME)

        if data.empty:
            print("No expenses found.")
            return

        amounts = np.array(data["amount"])

        print("Total Expense: ₹", np.sum(amounts))

    except FileNotFoundError:
        print("No expenses found.")


def analyze_expenses():
    try:
        data = pd.read_csv(FILE_NAME)

        if data.empty:
            print("No expenses found.")
            return

        amounts = np.array(data["amount"])

        print("\n===== EXPENSE ANALYSIS =====")
        print("Number of Expenses:", len(amounts))
        print("Total Expense: ₹", np.sum(amounts))
        print("Average Expense: ₹", round(np.mean(amounts), 2))
        print("Highest Expense: ₹", np.max(amounts))
        print("Lowest Expense: ₹", np.min(amounts))

        print("\n===== CATEGORY-WISE EXPENSE =====")

        category_total = data.groupby("category")["amount"].sum()

        print(category_total)

        highest_category = category_total.idxmax()

        print("\nHighest Spending Category:", highest_category)
        print("Amount Spent: ₹", category_total.max())

    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n===== EXPENSE TRACKER V4 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Expense")
    print("5. Analyze Expenses")
    print("6. Exit")

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
        analyze_expenses()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
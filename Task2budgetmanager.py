import os
import json
from datetime import datetime


TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r') as file:
            return json.load(file)
    return {"income": [], "expenses": []}

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as file:
        json.dump(transactions, file, indent=2)

def display_menu():
    print("\n=== Budget Tracker ===")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

def record_income(transactions):
    amount = float(input("Enter the income amount: "))
    category = input("Enter the income category: ")
    transactions["income"].append({"amount": amount, "category": category, "date": str(datetime.now())})
    print("Income recorded successfully!")

def record_expense(transactions):
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    transactions["expenses"].append({"amount": amount, "category": category, "date": str(datetime.now())})
    print("Expense recorded successfully!")

def view_budget(transactions):
    income_total = sum(item["amount"] for item in transactions["income"])
    expenses_total = sum(item["amount"] for item in transactions["expenses"])
    remaining_budget = income_total - expenses_total

    print("\n=== Budget Overview ===")
    print(f"Income: ${income_total:.2f}")
    print(f"Expenses: ${expenses_total:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def view_expense_analysis(transactions):
    expense_categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount

    print("\n=== Expense Analysis ===")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount:.2f}")

def main():
    transactions = load_transactions()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            record_income(transactions)
        elif choice == "2":
            record_expense(transactions)
        elif choice == "3":
            view_budget(transactions)
        elif choice == "4":
            view_expense_analysis(transactions)
        elif choice == "5":
            save_transactions(transactions)
            print("Exiting Budget Tracker. Have a good day!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

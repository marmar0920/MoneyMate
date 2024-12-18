import json
from datetime import datetime
from os.path import exists


DATA_FILE = "moneymate_data.json"


data = {
    "income": [],
    "expenses": [],
    "budgets": {},
    "savings_goals": {}
}


if exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
if not exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
else:
    with open(DATA_FILE, "r") as file:
        data = json.load(file)

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def log_income():
    amount = float(input("Enter income amount: $"))
    description = input("Enter a description for this income: ")
    entry = {"amount": amount, "description": description, "date": datetime.now().isoformat()}
    data["income"].append(entry)
    save_data()
    print("Income logged successfully.\n")


def log_expense():
    amount = float(input("Enter expense amount: $"))
    category = input("Enter category for this expense: ")
    description = input("Enter a description for this expense: ")
    entry = {"amount": amount, "category": category, "description": description, "date": datetime.now().isoformat()}
    data["expenses"].append(entry)
    save_data()
    print("Expense logged successfully.\n")


def set_budget():
    category = input("Enter category for the budget: ")
    amount = float(input(f"Enter budget amount for {category}: $"))
    data["budgets"][category] = amount
    save_data()
    print(f"Budget set for {category} at ${amount}.\n")


def set_savings_goal():
    goal_name = input("Enter the name of the savings goal: ")
    target_amount = float(input(f"Enter target amount for '{goal_name}': $"))
    data["savings_goals"][goal_name] = {"target": target_amount, "saved": 0}
    save_data()
    print(f"Savings goal '{goal_name}' set for ${target_amount}.\n")


def add_to_savings_goal():
    goal_name = input("Enter the name of the savings goal to add to: ")
    if goal_name in data["savings_goals"]:
        amount = float(input(f"Enter amount to add to '{goal_name}': $"))
        data["savings_goals"][goal_name]["saved"] += amount
        save_data()
        print(f"Added ${amount} to '{goal_name}'.\n")
    else:
        print(f"Savings goal '{goal_name}' does not exist.\n")

def validate_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value must be a positive number. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_summary():
    print("\n--- Financial Summary ---")
    
 
    total_income = sum(item["amount"] for item in data["income"])
    print(f"Total Income: ${total_income:.2f}")
    
  
    total_expenses = sum(item["amount"] for item in data["expenses"])
    print(f"Total Expenses: ${total_expenses:.2f}")
  
    category_expenses = {}
    for expense in data["expenses"]:
        category = expense["category"]
        category_expenses[category] = category_expenses.get(category, 0) + expense["amount"]
    
    print("\nExpenses by Category:")
    for category, amount in category_expenses.items():
        print(f" - {category}: ${amount:.2f} of ${data['budgets'].get(category, 'No budget set')}")
    
   
    print("\nSavings Goals:")
    for goal, details in data["savings_goals"].items():
        target = details["target"]
        saved = details["saved"]
        print(f" - {goal}: ${saved:.2f} of ${target} ({(saved / target * 100):.1f}%)")
    
  
    print(f"\nOverall Balance: ${total_income - total_expenses:.2f}")
    print("--- End of Summary ---\n")

    print("\nRemaining Budget by Category:")
    for category, budget in data["budgets"].items():
        spent = category_expenses.get(category, 0)
        remaining = budget - spent
        print(f" - {category}: ${remaining:.2f} remaining")

def progress_bar(current, total, length=20):
    proportion = int((current / total) * length)
    bar = "[" + "#" * proportion + "-" * (length - proportion) + "]"
    return bar
    for goal, details in data["savings_goals"].items():
    print(f" - {goal}: {progress_bar(details['saved'], details['target'])} {details['saved']:.2f}/{details['target']:.2f}")
def main_menu():
    print("Welcome to MoneyMate! Select an option:")
    while True:
        print("""
        1. Log Income
        2. Log Expense
        3. Set Budget
        4. Set Savings Goal
        5. Add to Savings Goal
        6. View Financial Summary
        7. Exit
        """)
        choice = input("Enter choice (1-7): ")
        
        if choice == "1":
            log_income()
        elif choice == "2":
            log_expense()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            set_savings_goal()
        elif choice == "5":
            add_to_savings_goal()
        elif choice == "6":
            view_summary()
        elif choice == "7":
            print("Exiting MoneyMate. Have a great day!")
            break
        else:
        print("Invalid choice. Please enter a number from 1 to 7.\n")

    search_term = input("Enter a keyword to search for expenses: ").lower()
    results = [e for e in data["expenses"] if search_term in e["description"].lower()]
    if results:
        print("\nMatching Expenses:")
        for e in results:
            print(f" - ${e['amount']:.2f} for {e['description']} (Category: {e['category']}, Date: {e['date']})")
    else:
        print("No matching expenses found.\n")
if __name__ == "__main__":
    main_menu()

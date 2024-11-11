# MoneyMate
MoneyMate is a simple, web-based personal finance tracker that helps users log income and expenses, set budgets, and track savings goals. Built with Flask and styled with a feminine, pink-themed design, MoneyMate is ideal for individuals who want an intuitive and elegant way to manage their finances.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage Guide](#usage-guide)
- [Styling](#styling)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
## Features

- **Log Income:** Easily record income entries with amount and description.
- **Log Expenses:** Track expenses by amount, category, and description.
- **Set Budgets:** Define budgets for spending categories and monitor spending against set limits.
- **Set Savings Goals:** Set and track progress toward specific financial goals with customs goal names and targets.
- **View Financial Summary:** Get an overview of total income, total expenses, budget usage, and savings goal progress.
## Project Structure

```plaintext
MoneyMate/
│
├── app.py                  # Main Flask application file
├── moneymate_data.json     # JSON file for data storage
├── templates/              # HTML templates folder
│   ├── index.html          # Homepage
│   ├── log_income.html     # Log income page
│   ├── log_expense.html    # Log expense page
│   ├── set_budget.html     # Set budget page
│   ├── set_goal.html       # Set savings goal page
│   └── summary.html        # Financial summary page
└── static/                 # Static files folder
    └── style.css           # CSS file for styling
```

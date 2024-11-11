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
## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Data Storage:** JSON file (`moneymate_data.json`)
- **Styling:** Google Fonts (Playfair Display), Custom CSS
## Setup Instructions

### Prerequisites

- **Python 3.x** is required. Install Python from [python.org](https://www.python.org/downloads/) if you haven’t already.
- **pip** (Python package manager) should be installed along with Python.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/MoneyMate.git
cd MoneyMate
```

### 2. Install Flask

Install Flask using pip:

```bash
pip install flask
```

### 3. Run the Application

Start the Flask server by running:

```bash
python app.py
```

You should see output indicating that the Flask server is running, with a message like this:

```plaintext
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 4. Open the Application

In your web browser, navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the MoneyMate app.

## Usage Guide

### Homepage

On the homepage, you’ll find links to navigate through different functionalities:

- **Log Income**
- **Log Expense**
- **Set Budget**
- **Set Savings Goal**
- **View Summary**


from db import init_db
from logic import add_expense, view_expenses, summary, delete_expense

init_db()

while True:
    print("""
    === Personal Expense Tracker ===
    1. Add Expense
    2. View All Expenses
    3. Summary by Category
    4. Delete an Expense
    5. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        desc = input("Description: ")
        add_expense(date, category, amount, desc)
        print("Expense added successfully.")
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        summary()
    elif choice == '4':
        eid = int(input("Enter expense ID to delete: "))
        delete_expense(eid)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

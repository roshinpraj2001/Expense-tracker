import sqlite3
from tabulate import tabulate

def add_expense(date, category, amount, desc):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                (date, category, amount, desc))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Date", "Category", "Amount", "Description"], tablefmt="grid"))
    conn.close()

def summary():
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cur.fetchall()
    print("\n--- Summary by Category ---")
    print(tabulate(rows, headers=["Category", "Total Amount"], tablefmt="fancy_grid"))
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()
    print("Expense deleted.")

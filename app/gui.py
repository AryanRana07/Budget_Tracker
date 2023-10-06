import tkinter as tk
from tkinter import ttk
from expense import Expenses
from budget_manager import BudgetManager

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data-Driven Expense Tracker")
        
        # Create and position widgets (buttons, labels, entry fields)
        
        # Label for category
        self.label_category = tk.Label(self.root, text="Expense Category:")
        self.label_category.grid(row=0, column=0, padx=10, pady=10)
        
        # Dropdown for expense category
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.root, textvariable=self.category_var)
        self.category_combobox['values'] = ["Groceries", "Entertainment", "Bills"]
        self.category_combobox.grid(row=0, column=1, padx=10, pady=10)
        
        # Label for date
        self.label_date = tk.Label(self.root, text="Expense Date:")
        self.label_date.grid(row=1, column=0, padx=10, pady=10)
        
        # Entry field for date
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Label for amount
        self.label_amount = tk.Label(self.root, text="Expense Amount:")
        self.label_amount.grid(row=2, column=0, padx=10, pady=10)
        
        # Entry field for amount
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Label for description
        self.label_description = tk.Label(self.root, text="Expense Description:")
        self.label_description.grid(row=3, column=0, padx=10, pady=10)
        
        # Entry field for description
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Button to add an expense
        self.add_expense_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=4, columnspan=2, padx=10, pady=10)
        
        # Listbox to display expenses
        self.expense_listbox = tk.Listbox(self.root)
        self.expense_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        # TODO: Add other widgets for budget management, insights, etc.

    def add_expense(self):
        # Implement the logic for adding expenses here
        # Get values from the input fields
        category = self.category_var.get()
        date = self.date_entry.get()
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        
        # Create an Expense instance (you should implement this part)
        new_expense = Expenses(category, date, amount, description)
        
        # TODO: Add the expense to the budget manager or database
        
        # TODO: Update the listbox or display a message to confirm the expense addition

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

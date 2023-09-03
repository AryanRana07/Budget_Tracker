from expense import Expense
from budget_manager import BudgetManager

expense1 = Expense (category="Groceries", date="2023-08-01", amount = 50, description="Weekly Groceries")

budget_manager = BudgetManager()

budget_manager.set_budget(category = "Groceries" , amount = 200)

print(f"Exense Category: {expense1.category}")
print(f"Expense Amount: ${expense1.amount}")
print(f"Budget for {expense1.category}: ${budget_manager.budget.get(expense1.category,'N/A')}")
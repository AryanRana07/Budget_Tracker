class BudgetManager:
    def __init__(sellf):
        self.budget = {}
        
    def set_budget(self, amount, category):
        self.budget[category] = amount
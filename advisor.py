def financial_advice(income, expenses, goal):

    savings = income - expenses

    if savings <= 0:
        return "Your expenses are higher than your income. Try reducing expenses."

    emergency_fund = savings * 0.2
    investments = savings * 0.3
    savings_plan = savings * 0.5

    advice = f"""
Monthly Savings Available: ${savings}

Suggested Allocation:
Savings: ${savings_plan}
Investments: ${investments}
Emergency Fund: ${emergency_fund}

Financial Goal: {goal}
"""

    return advice

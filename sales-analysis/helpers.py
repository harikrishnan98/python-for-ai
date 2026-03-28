
def calculate_total(quantity, price):
    """Calculate Total for single item"""
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"
def calculate_total(prices):
    total_bill=sum(prices)
    return total_bill

def apply_tax(amount):
    tax_amount=amount+(amount*0.05)
    return tax_amount
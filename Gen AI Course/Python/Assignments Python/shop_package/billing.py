def calculate_total(prices):
    total=0
    for i in prices:
        total+=i
    return total

def apply_tax (amount):
    return (amount + (amount*0.05))
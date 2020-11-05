meal_price = int(input ("Enter the meal price : "))
tip_percent = 20
tax_percent = 8

def bill(meal_price,tip_percent, tax_percent):
    tip = meal_price * tip_percent /100
    tax = meal_price * tax_percent /100
    total_price = round(meal_price + tip + tax)
    return total_price

print("Your total price is",bill(meal_price,tip_percent, tax_percent))

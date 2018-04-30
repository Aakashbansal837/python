meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())
total=meal_cost
tip = total*(tip_percent/100)
tax = total*(tax_percent/100)
total=total+tip+tax
total=round(total)
print("The total meal cost is {} dollars.".format(total))

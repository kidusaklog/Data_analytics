##Lab 1 — Restaurant tip script
# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# str() converts a number to a string so it can be joined with other strings using +
# print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))


##Lab 2 — Math scripts 
##net_worth
assets = 50000
debts = 15000
net_worth = assets - debts

print("Your total assets are " + str(assets))
print("Your total debts are " + str(debts))
print("Your net worth is " + str(net_worth))


##area_of_rectangle
side_a = 12
side_b = 19
area = side_a * side_b

print("Side A is " + str(side_a))
print("Side B is " + str(side_b))
print("The area of the rectangle is " + str(area))

##tip_amount
bill = 55.00
tip_percentage = 0.18
tip = bill * tip_percentage

print("The tip on a $" + str(bill) + " restaurant bill is $" + format(tip, ".2f"))

##area_of_circle

import math

diameter = 19
radius = diameter / 2
area = math.pi * radius ** 2

print("The area of a circle with radius " + str(radius) + " is " + format(area, ".2f"))

##rule_of_72

savings = 5000
interest_rate = 0.06
years = 72 / (interest_rate * 100)
doubled = savings * 2
print("Your current savings is " + str(savings))
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth " + format(doubled, ".2f")+ " in " + format(years, ".1f") + " years")







##Lab 3 — Add input


bill = float(input("What was your restaurant bill? "))
tip_percentage = float(input("What percentage do you want to tip? (e.g. 0.18 for 18%) "))
tip = bill * tip_percentage

print("The tip on a $" + str(bill) + " restaurant bill is $" + format(tip, ".2f"))

# Pitfall: input() always returns a string, so you MUST wrap it in float() or int()
# if you want to do math with it, otherwise you'll get an error!




##Lab 4 — Rewrite with f-strings

bill = float(input("What was your restaurant bill? "))
tip_percentage = float(input("Tip percentage? (e.g. 0.18) "))
tip = bill * tip_percentage

print(f"The tip on a ${bill} restaurant bill is ${format(tip, '.2f')}")
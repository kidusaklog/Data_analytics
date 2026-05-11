#lab1
# Demonstrates a for loop iterating through a list of words

great_words = ["amazing", "awesome", "excellent", "fantastic", "outstanding", "incredible", "brilliant"]

for word in great_words:
    print(f"Loops are {word}!")

print("I <3 loops")






#lab2
# Uses a while loop to track savings progress toward a goal

starting_balance = 500.00
savings_goal    = 2000.00
weekly_savings  = 150.00
treat_cost      = 20.00     # cost of a small treat when balance hits 75% of goal

bank_balance = starting_balance

print(f"Starting balance:  ${bank_balance:,.2f}")
print(f"Savings goal:      ${savings_goal:,.2f}")
print(f"Weekly savings:    ${weekly_savings:,.2f}")
print("-" * 45)

while bank_balance < savings_goal:
    bank_balance += weekly_savings

    halfway  = savings_goal * 0.50
    almost   = savings_goal * 0.75

    if bank_balance >= almost:
        # Buy a little treat
        bank_balance -= treat_cost
        print(f"So close! After treating myself, my balance is up to ${bank_balance:,.2f}")
    elif bank_balance >= halfway:
        print(f"Almost there! This week my balance is up to ${bank_balance:,.2f}")
    else:
        print(f"This week my balance increased to ${bank_balance:,.2f}")

print("-" * 45)
print(f"Goal met! My current balance is ${bank_balance:,.2f}")





#lab3
# Uses enumerate() with a for loop to print a numbered ranked list

favorite_foods = ["injera", "jollof rice", "tibs", "shiro", "kitfo", "doro wat", "ful"]

print("=== My Favorite Foods (ranked) ===")
for rank, food in enumerate(favorite_foods, start=1):
    if rank == 1:
        print(f"{rank}. {food} <- top pick!")
    else:
        print(f"{rank}. {food}")

# BONUS: Print the list in reverse order, still numbered 1 through len
print()
print("=== Bonus: Reverse Order (still numbered 1 to 7) ===")
for rank, food in enumerate(reversed(favorite_foods), start=1):
    if rank == 1:
        print(f"{rank}. {food} <- top pick!")
    else:
        print(f"{rank}. {food}")




#lab4
# Loops through sales data tuples and identifies top performers

sales_data = [
    ('Marcus Webb',    'East',  4250.00),
    ('Priya Sharma',   'West',  5875.50),
    ('DeShawn Carter', 'East',  3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen',     'West',  4980.25),
]

# BONUS: track total sales before the loop
total_sales = 0.00

print("=== Monthly Sales Report ===")
for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")
    if sales > 5000:
        print("  ^ Top performer!")
    total_sales += sales

# BONUS: print overall total after the loop
print("-" * 35)
print(f"Total sales across all reps: ${total_sales:,.2f}")
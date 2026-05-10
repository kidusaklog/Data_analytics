# ╔══════════════════════════════════════════╗
# ║         KIDUS TESEMA                     ║
# ║    ~ Year Up United Student ~            ║
# ║       Data Analytics Track               ║
# ╚══════════════════════════════════════════╝
# Exercise 4A - Using Conditionals


##Lab 1 - Using conditionals
x = 100
y = 20

# a) If x divided by y is 5, print message and set x to 1
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")

# b) If x times y is y, print message and set x to 10
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("boombambaper, x equals " + str(x))

# c) If x is less than y, print message and double x
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("yarayara, x is not less than y")

# d) If x is greater than y, print message - otherwise print other message
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

# e) Final print statement showing final values
print("The final value of x is " + str(x) + " and the final value of y is " + str(y))








# Lab 2 - Gross Pay Calculator with Overtime


pay_rate = 17.30
hours_worked = 45

# Constants
REGULAR_HOURS_LIMIT = 40
OVERTIME_MULTIPLIER = 1.5

# Calculate gross pay
if hours_worked > REGULAR_HOURS_LIMIT:
    regular_pay = pay_rate * REGULAR_HOURS_LIMIT
    overtime_hours = hours_worked - REGULAR_HOURS_LIMIT
    overtime_pay = pay_rate * OVERTIME_MULTIPLIER * overtime_hours
    gross_pay = regular_pay + overtime_pay
    print("Hours worked: " + str(hours_worked))
    print("Regular pay (" + str(REGULAR_HOURS_LIMIT) + " hrs): $" + str(regular_pay))
    print("Overtime hours: " + str(overtime_hours))
    print("Overtime pay: $" + str(overtime_pay))
else:
    gross_pay = pay_rate * hours_worked
    print("Hours worked: " + str(hours_worked))
    print("No overtime.")

print("Gross Pay: $" + str(round(gross_pay, 2)))

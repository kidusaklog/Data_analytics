# ╔══════════════════════════════════════════╗
# ║         KIDUS TESEMA                     ║
# ║    ~ Year Up United Student ~            ║
# ║       Data Analytics Track               ║
# ╚══════════════════════════════════════════╝
# 
# ##lab1 

dept_code = 18  # Change this value to test different codes

if dept_code == 1:
    dept_name = "Marketing"
elif dept_code == 5:
    dept_name = "Human Resources"
elif dept_code == 10:
    dept_name = "Accounting"
elif dept_code == 12:
    dept_name = "Legal"
elif dept_code == 18:
    dept_name = "IT"
elif dept_code == 20:
    dept_name = "Customer Relations"
else:
    dept_name = "Unknown Department"

print("Department Code: " + str(dept_code))
print("Department Name: " + dept_name)


#lab2
# greeting
# Time-based Greeting Script

hour = 23  # Change this value to test (0-23)

print("Current hour: " + str(hour) + ":00")

# Part 1 & 2 combined: greetings based on hour
if hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")

# Part 2: Late night condition (11pm = 23, through 4am = 4)
if hour >= 23 or hour < 4:
    print("What are you doing up so late??")




#lab 3 
# complex_taxes.py

# ---------- Pay variables ----------
pay_rate = 17.30
hours_worked = 45
filing_status = 'single'   # change to 'joint' to test joint filer table

# ---------- Gross pay calculation (weekly) ----------
REGULAR_HOURS_LIMIT = 40
OVERTIME_MULTIPLIER = 1.5
WEEKS_IN_YEAR = 52

if hours_worked > REGULAR_HOURS_LIMIT:
    regular_pay = pay_rate * REGULAR_HOURS_LIMIT
    overtime_hours = hours_worked - REGULAR_HOURS_LIMIT
    overtime_pay = pay_rate * OVERTIME_MULTIPLIER * overtime_hours
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = pay_rate * hours_worked

# ---------- Annual gross pay ----------
annual_gross = weekly_gross * WEEKS_IN_YEAR

# ---------- Tax rate lookup ----------
if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    tax_rate = 0.00
    print("Unknown filing status. No tax applied.")

# ---------- Weekly tax and net pay ----------
weekly_tax = weekly_gross * tax_rate
net_pay = weekly_gross - weekly_tax

# ---------- Output ----------
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${weekly_gross:.2f}")
print(f"Your estimated annual gross pay is ${annual_gross:,.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax rate is {tax_rate:.0%}")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is ${net_pay:.2f}")    







##lab 4
# min_max.py
# Displays the smallest and largest of three numbers using if/else statements

a = 42
b = 17
c = 85

# ---------- Find minimum ----------
if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

# ---------- Find maximum ----------
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

# ---------- Output ----------
print(f"The three numbers are: {a}, {b}, {c}")
print(f"The smallest number is: {minimum}")
print(f"The largest number is:  {maximum}")







##lab 5
# show_major.py
# Displays major name and department office based on a major code

student_name = "Bitanya Abebe"
student_major = "CSCI"   # Change to test: BIOL, CSCI, ENG, HIST, MKT, or unknown

# ---------- Major code lookup ----------
if student_major == "BIOL":
    major_name = "Biology"
    department_office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    department_office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    department_office = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    department_office = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    department_office = "Westly Hall, Room 310"
else:
    major_name = "<unknown>"
    department_office = ""

# ---------- Output ----------
print(f"Student Name:  {student_name}")
print(f"Major Code:    {student_major}")
print(f"Major Name:    {major_name}")
if department_office:
    print(f"Dept. Office:  {department_office}")
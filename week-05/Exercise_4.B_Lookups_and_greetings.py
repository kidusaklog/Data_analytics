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




    
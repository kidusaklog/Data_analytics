# ============================================
# Pi Birthday Checker
# Kidus's Birthday: March 4, 2002 (030402)
# ============================================

# Step 1 - Load all lines from pi file
pi = open("pi_million_digits_bonus.txt", "r")
pi_lines = pi.readlines()
pi.close()

# Step 2 - Print first line to confirm file loaded
pi = open("pi_million_digits_bonus.txt", "r")
print("First line of pi:", pi.readline())
pi.close()

# Step 3 - Build one clean long string of pi
pi_string = ""
for i in pi_lines:
    pi_string += i.strip()  # removes spaces and \n from each line

print("First 50 chars of pi_string:", pi_string[0:50])

# ─────────────────────────────────────────
# Version 1 - Basic check (no message if not found)
# ─────────────────────────────────────────
def pi_bday_check(bday):
    for i in pi_lines:
        if bday in i:
            print("Your birthday is in the first million digits of pi!")
            break

# ─────────────────────────────────────────
# Version 2 - With not-found message
# ─────────────────────────────────────────
def pi_bday_check2(bday):
    birthday_found = 0  # tracker variable

    for i in pi_lines:
        if bday in i:
            print("Your birthday is in the first million digits of pi!")
            birthday_found += 1
            break

    if birthday_found != 1:
        print("Sorry, your birthday was not found in the first million digits of pi")

# ─────────────────────────────────────────
# Version 3 - With position finder (final version)
# ─────────────────────────────────────────
def pi_bday_check3(bday):
    birthday_found = 0
    bday_position = ""  # local position tracker

    for i in pi_lines:
        if bday in i:
            print("Your birthday is in the first million digits of pi!")
            birthday_found += 1
            break

    if birthday_found != 1:
        print("Sorry, your birthday was not found in the first million digits of pi")
    else:
        # -1 because pi_string starts with "3." so we subtract the "3" before decimal
        bday_position = pi_string.index(bday) - 1
        print(f"Your birthday begins at decimal place {bday_position}")

# ─────────────────────────────────────────
# Run the check for Kidus's birthday
# 03/04/2002 → MMDDYY format → "030402"
# ─────────────────────────────────────────
print("\n--- Checking Kidus's Birthday: March 4, 2002 ---")
pi_bday_check3("030402")

# Bonus: test a few others
print("\n--- Testing other birthdays ---")
pi_bday_check3("070281")   # Jul 2 1981     ✅ should be found
pi_bday_check3("112901")   # Nov 29 2001    ❌ should not be found

# ============================================
# Exercise 4.B Lab 1 - Exception Basics
# ============================================


# ─────────────────────────────────────────
# 1. ValueError - right type, wrong value
# ─────────────────────────────────────────
try:
    age = int("Kidus")          # string can't be converted to int
except ValueError:
    print("ValueError: Can't convert that string into a number")
else:
    print(f"Age is: {age}")
finally:
    print("Let's try another one...\n")

# Second way to get ValueError
try:
    number = int("030402")      # this actually works! MMDDYY = valid digits
    int("March 4")              # this does NOT work
except ValueError:
    print("ValueError: 'March 4' is not a valid integer")
else:
    print(f"Number is: {number}")
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# 2. NameError - variable used before defined
# ─────────────────────────────────────────
try:
    m = banana                  # banana is never defined anywhere
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# Second way to get NameError
try:
    print(city)                 # city was never assigned
except NameError:
    print("NameError: Variable 'city' is not defined")
else:
    print(f"City is: {city}")
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# 3. TypeError - wrong data type for operation
# ─────────────────────────────────────────
try:
    result = "Kidus" + 24       # can't add string and integer together
except TypeError:
    print("TypeError: Can't concatenate a string and an integer")
else:
    print(f"Result is: {result}")
finally:
    print("Let's try another one...\n")

# Second way to get TypeError
try:
    result = len(24)            # len() doesn't work on integers
except TypeError:
    print("TypeError: object of type 'int' has no len()")
else:
    print(f"Length is: {result}")
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# 4. SyntaxError - invalid Python syntax
# Note: SyntaxError happens BEFORE code runs,
# so we use exec() to catch it at runtime
# ─────────────────────────────────────────
try:
    exec("if True print('hello')")   # missing colon after if
except SyntaxError:
    print("SyntaxError: Invalid syntax — missing colon after 'if'")
else:
    print("No syntax error!")
finally:
    print("Let's try another one...\n")

# Second way to get SyntaxError
try:
    exec("def greet(name")           # missing closing parenthesis
except SyntaxError:
    print("SyntaxError: Missing closing parenthesis in function definition")
else:
    print("No syntax error!")
finally:
    print("All done! Great job Kidus!\n")

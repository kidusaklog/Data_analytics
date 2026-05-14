# ── Function 1: display_mailing_label ───────────────────────────────────────
# Parameters: name, address, city, state, zip
# Formats and displays data as a mailing address label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")
    print()  # blank line between labels

# ── Function 2: add_numbers ──────────────────────────────────────────────────
# Uses *args to accept any number of integer arguments
# Adds them together and displays the equation with the result
def add_numbers(*args):
    result = sum(args)
    # Build the equation string: "num1 + num2 + ... = result"
    equation = ' + '.join(str(n) for n in args)
    print(f"{equation} = {result}")

# ── Function 3: display_receipt ──────────────────────────────────────────────
# Parameters: total_due, amount_paid
# Displays total, amount paid, and change due (or remaining balance)
def display_receipt(total_due, amount_paid):
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")
    print()  # blank line between receipts

# ── BONUS: display_mailing_label2 ────────────────────────────────────────────
# Adds an optional second address line (apartment, suite, c/o, etc.)
# address2 defaults to None so the function still works with one address line
def display_mailing_label2(name, address, city, state, zip, address2=None):
    print(name)
    print(address)
    if address2:
        print(address2)
    print(f"{city}, {state} {zip}")
    print()

# ── BONUS: display_receipt2 ──────────────────────────────────────────────────
# Uses *totals to accept one or more balance amounts for total_due
# Sums all totals, then computes change or remaining balance as before
def display_receipt2(amount_paid, *totals):
    total_due = sum(totals)
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")
    print()


# ════════════════════════════════════════════════════════════════════════════
# FUNCTION CALLS
# ════════════════════════════════════════════════════════════════════════════

# ── display_mailing_label calls ──────────────────────────────────────────────
print("=== Mailing Labels ===")
display_mailing_label('Rebecca Yang', '123 Oak Street', 'Chicago', 'IL', '60601')
display_mailing_label('Marcus Rivera', '456 Elm Avenue', 'Austin', 'TX', '78701')

# ── add_numbers calls ────────────────────────────────────────────────────────
print("=== Adding Numbers ===")
add_numbers(7)                      # one number
add_numbers(12, 8)                  # two numbers
add_numbers(5, 10, 15, 20, 25)      # five numbers

print()

# ── display_receipt calls ────────────────────────────────────────────────────
print("=== Receipts ===")
display_receipt(45.00, 60.00)   # overpay  -> change due
display_receipt(45.00, 45.00)   # exact    -> $0.00 change
display_receipt(45.00, 20.00)   # underpay -> remaining balance

# ── BONUS calls ──────────────────────────────────────────────────────────────
print("=== BONUS: Two-line Mailing Label ===")
display_mailing_label2('Acme Corp', '789 Pine Road', 'Seattle', 'WA', '98101',
                        address2='Suite 400')

print("=== BONUS: Receipt with Multiple Balances ===")
display_receipt2(100.00, 30.00, 25.00, 40.00)  # three balances totaling $95, paid $100

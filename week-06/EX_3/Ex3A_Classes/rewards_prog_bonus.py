# cust_list is created once here at the global (module) level.
# This ensures that each call to add_to_cust_list() appends to the same list
# rather than creating a new one every time an instance is made or the method runs.
cust_list = []


class RewardsProgram:
    '''Represents a restaurant rewards program member.
    Stores customer contact information and provides methods to display
    a profile, print a thank-you message, and add the customer to a
    shared customer list.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone     = phone
        self.email     = email

    def profile(self):
        '''Prints the customer's contact information.'''
        print(f"Name:  {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        '''Prints a personalised thank-you message.'''
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        '''Appends the customer's details as a tuple to the global cust_list.
        The global keyword lets us modify the module-level list from inside the method.'''
        global cust_list
        cust_list.append((self.cust_name, self.phone, self.email))


# ── Create three customer instances ─────────────────────────────────────────
customer_1 = RewardsProgram('Maria Lopez',  '312-555-0192', 'maria.lopez@email.com')
customer_2 = RewardsProgram('James Carter', '773-555-0384', 'jcarter@email.com')
customer_3 = RewardsProgram('Aisha Patel',  '847-555-0571', 'aisha.patel@email.com')

# ── Run all three methods for each customer ──────────────────────────────────
print("── Customer 1 ──────────────────────")
customer_1.profile()
customer_1.thank_you()
customer_1.add_to_cust_list()

print("\n── Customer 2 ──────────────────────")
customer_2.profile()
customer_2.thank_you()
customer_2.add_to_cust_list()

print("\n── Customer 3 ──────────────────────")
customer_3.profile()
customer_3.thank_you()
customer_3.add_to_cust_list()

# ── Print the full customer list to confirm all three were added ─────────────
print("\n── Full Customer List ──────────────")
for customer in cust_list:
    print(customer)

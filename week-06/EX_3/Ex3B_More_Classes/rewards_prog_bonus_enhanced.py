cust_list = []


class RewardsProgram:
    '''Represents a restaurant rewards program member.
    Tracks restaurants visited, calculates rewards points per visit
    (at a rate of $1 = 1 point, rounded down), and maintains a
    per-restaurant points balance stored as a dictionary.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name          = cust_name
        self.phone              = phone
        self.email              = email
        self.restaurants_visited = []
        # CHALLENGE: store points as a dict keyed by restaurant name
        # so we can track the balance per restaurant separately
        self.rewards_points     = {}   # { 'restaurant name': points_balance }

    def profile(self):
        print(f"Name:  {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        global cust_list
        cust_list.append((self.cust_name, self.phone, self.email))

    # ── CHALLENGE: separate method just for points calculation ───────────────
    def calculate_rewards(self, bill_amount):
        '''Converts a dollar bill amount to whole reward points (floor, $1 = 1 pt).'''
        import math
        return math.floor(bill_amount)

    def visit_rest(self):
        '''Records a restaurant visit, awards points, and prints a summary.
        Points are stored per restaurant in a dictionary so each location
        has its own running balance.'''
        rest_name = input("Name of restaurant: ").strip()

        # Add to visited list only if not already there
        if rest_name not in self.restaurants_visited:
            self.restaurants_visited.append(rest_name)

        bill_raw = input("What was the total food bill for this visit? $")
        try:
            bill_amount = float(bill_raw)
        except ValueError:
            print("Invalid amount entered. No points awarded for this visit.")
            return

        points_earned = self.calculate_rewards(bill_amount)

        # Update the per-restaurant points balance in the dictionary
        if rest_name in self.rewards_points:
            self.rewards_points[rest_name] += points_earned
        else:
            self.rewards_points[rest_name] = points_earned

        total_points = sum(self.rewards_points.values())

        print(f"Points for this visit: {points_earned}")
        print(f"Total rewards points earned: {total_points}")
        print(f"Thank you for visiting {rest_name}!")
        print()


# ── Three customer instances ─────────────────────────────────────────────────
customer_1 = RewardsProgram('Maria Lopez',  '312-555-0192', 'maria.lopez@email.com')
customer_2 = RewardsProgram('James Carter', '773-555-0384', 'jcarter@email.com')
customer_3 = RewardsProgram('Aisha Patel',  '847-555-0571', 'aisha.patel@email.com')

for customer in [customer_1, customer_2, customer_3]:
    print(f"── {customer.cust_name} ──────────────────────")
    customer.profile()
    customer.thank_you()
    customer.add_to_cust_list()
    customer.visit_rest()
    customer.visit_rest()
    print(f"Restaurants visited: {customer.restaurants_visited}")
    print(f"Points by restaurant: {customer.rewards_points}")
    print()

print("── Full Customer List ──────────────")
for c in cust_list:
    print(c)

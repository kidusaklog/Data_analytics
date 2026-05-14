class Restaurant:
    '''Represents a restaurant with a name and food type.
    Tracks customers served, accepts new customer counts, and collects
    customer ratings with running average calculation.'''

    def __init__(self, rest_name, food_type):
        self.rest_name        = rest_name
        self.food_type        = food_type
        self.number_served    = 0
        # NOTE: default mutable attributes like lists must be set here in __init__,
        # not as a class-level default, to ensure each instance gets its own list.
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        '''Prompts for customers served today and adds to the running total.'''
        amount = input("How many customers were served today? ")
        try:
            self.number_served += int(amount)
        except ValueError:
            print("Please enter a whole number.")

    def print_num_served(self):
        '''Prints the total number of customers served so far.'''
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        '''Prompts for a 1-5 integer rating, validates the input, adds it to
        the ratings list, and prints the rating alongside the updated average.'''
        while True:
            raw = input("How would you rate your experience today on a scale of 1-5 "
                        "(5 being excellent)? ")
            # Check 1: make sure the input can be converted to a number at all
            try:
                value = float(raw)
            except ValueError:
                print("Invalid input — please enter a whole number between 1 and 5.")
                continue

            # Check 2: make sure it is a whole number (no decimals like 2.5)
            if value != int(value):
                print("Please enter a whole number, not a decimal.")
                continue

            rating = int(value)

            # Check 3: make sure it falls within the valid 1-5 range
            if rating < 1 or rating > 5:
                print("Rating must be between 1 and 5. Please try again.")
                continue

            # All checks passed — record the rating and report the average
            self.customer_ratings.append(rating)
            average = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. "
                  f"The average rating for {self.rest_name} is {average:.1f}.")
            break


# ── Three restaurant instances ───────────────────────────────────────────────
restaurant_1 = Restaurant('The Pasta House', 'Italian food')
restaurant_2 = Restaurant('Golden Dragon',   'Chinese food')
restaurant_3 = Restaurant('Taco Loco',       'Mexican food')

# ── Test print_num_served → add_num_served → print_num_served ────────────────
print("=== Customers Served ===")
for rest in [restaurant_1, restaurant_2, restaurant_3]:
    rest.print_num_served()          # initial value: 0
    rest.add_num_served()            # first input
    rest.add_num_served()            # second input
    rest.print_num_served()          # updated total
    print()

# ── Test customer_rating (including invalid inputs) ───────────────────────────
print("=== Customer Ratings ===")
for rest in [restaurant_1, restaurant_2, restaurant_3]:
    print(f"\nRatings for {rest.rest_name}:")
    rest.customer_rating()
    rest.customer_rating()
    rest.customer_rating()

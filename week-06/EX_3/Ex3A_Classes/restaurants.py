class Restaurant:
    '''Represents a restaurant with a name and food type.
    Provides methods to describe the restaurant and indicate it is open.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# ── Create three instances ───────────────────────────────────────────────────
restaurant_1 = Restaurant('The Pasta House', 'Italian food')
restaurant_2 = Restaurant('Golden Dragon', 'Chinese food')
restaurant_3 = Restaurant('Taco Loco', 'Mexican food')

# ── Call both methods for each instance ─────────────────────────────────────
restaurant_1.describe_rest()
restaurant_1.rest_open()

print()

restaurant_2.describe_rest()
restaurant_2.rest_open()

print()

restaurant_3.describe_rest()
restaurant_3.rest_open()

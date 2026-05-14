class Restaurant:
    '''Represents a restaurant with a name and food type.
    Provides methods to describe the restaurant and indicate it is open.'''

    def __init__(self, rest_name, food_type):
        self.rest_name     = rest_name
        self.food_type     = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# ── Three Restaurant instances (unchanged from Lab 1) ────────────────────────
restaurant_1 = Restaurant('The Pasta House', 'Italian food')
restaurant_2 = Restaurant('Golden Dragon',   'Chinese food')
restaurant_3 = Restaurant('Taco Loco',       'Mexican food')

for rest in [restaurant_1, restaurant_2, restaurant_3]:
    rest.describe_rest()
    rest.rest_open()
print()


# ════════════════════════════════════════════════════════════════════════════
class FoodTruck(Restaurant):
    '''A child class of Restaurant representing a mobile food truck.
    Inherits name and food type from Restaurant, and adds attributes
    for private booking availability and current location.
    Also maintains a location history (unique locations only) so operators
    can see which areas the truck has previously served without cluttering
    the list with repeat visits to the same spot.'''

    def __init__(self, rest_name, food_type):
        # Call the parent __init__ to set rest_name and food_type
        super().__init__(rest_name, food_type)
        # Child-specific attributes
        self.private_bookings = 'N'
        self.truck_location   = ''
        # CHALLENGE: track location history as a list of unique locations.
        # We store unique entries only (no duplicates) because the history is
        # meant to show WHERE the truck has operated, not HOW MANY times it
        # visited each spot. If visit frequency were important, we could use a
        # dict of {location: visit_count} instead.
        self.location_history = []

    def accepts_private_bookings(self):
        '''Prompts the operator to set whether the truck takes private bookings.'''
        answer = input("Does this food truck accept private bookings? Y/N ").strip().upper()
        if answer == 'Y':
            self.private_bookings = 'Y'
            print("This food truck currently accepts private bookings.")
        elif answer == 'N':
            self.private_bookings = 'N'
            print("This food truck currently does not accept private bookings.")
        else:
            print("Please enter Y or N.")

    def relocate_truck(self):
        '''Prompts for the truck's current location and records it.
        Adds the location to history only if it is a new location.'''
        location = input("Enter the truck's current location (street address and city): ").strip()
        self.truck_location = location
        print(f"Truck is currently located at {location}.")

        # CHALLENGE: add to history only if not already recorded
        if location not in self.location_history:
            self.location_history.append(location)

    def print_location_history(self):
        '''Prints all unique locations the truck has operated from.'''
        if not self.location_history:
            print(f"{self.rest_name} has no location history yet.")
        else:
            print(f"{self.rest_name} location history:")
            for loc in self.location_history:
                print(f"  - {loc}")


# ── Two FoodTruck instances ───────────────────────────────────────────────────
truck_1 = FoodTruck('Rolling Tacos', 'Mexican street food')
truck_2 = FoodTruck('Wok on Wheels', 'Asian fusion')

# ── Test inherited methods ────────────────────────────────────────────────────
print("=== Food Trucks – inherited methods ===")
truck_1.describe_rest()
truck_1.rest_open()
truck_2.describe_rest()
truck_2.rest_open()
print()

# ── Test accepts_private_bookings ────────────────────────────────────────────
print("=== Private Bookings ===")
truck_1.accepts_private_bookings()
truck_2.accepts_private_bookings()
print()

# ── Test relocate_truck and location history ──────────────────────────────────
print("=== Relocations ===")
truck_1.relocate_truck()
truck_1.relocate_truck()   # enter the same address again to confirm no duplicate
truck_1.relocate_truck()   # enter a new address
truck_1.print_location_history()
print()

truck_2.relocate_truck()
truck_2.relocate_truck()
truck_2.print_location_history()

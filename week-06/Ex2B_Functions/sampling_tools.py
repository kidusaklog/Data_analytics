import random

# Starting product inventory list
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# a) Product of the Day - randomly select one product using random.choice()
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# b) Usability survey - select 3 unique products using random.sample() (no repeats)
survey_picks = random.sample(products, 3)
print(f"\nProducts selected for usability survey: {survey_picks}")

# c) Presentation order - shuffle all products in place using random.shuffle()
# Note: random.shuffle() modifies the list directly and returns None,
# so we print 'products' after shuffling, NOT the return value of shuffle()
random.shuffle(products)
print(f"\nProducts in randomized presentation order: {products}")

# d) Simulated daily transaction count - random integer between 50 and 300
daily_transactions = random.randint(50, 300)
print(f"\nSimulated daily transaction count: {daily_transactions}")

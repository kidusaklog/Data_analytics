# ╔══════════════════════════════════════════╗
# ║         KIDUS TESEMA                     ║
# ║    ~ Year Up United Student ~            ║
# ║       Data Analytics Track               ║
# ╚══════════════════════════════════════════╝

# Author: Kidus Tesema

## ============================================
## EX2B - LAB 1: FAHRENHEIT TO CELSIUS (f_to_c)
## ============================================

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F is equal to {format(celsius, '.2f')}°C")

## ============================================
## EX2B - LAB 2: CELSIUS TO FAHRENHEIT (c_to_f)
## ============================================

celsius = 37
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {format(fahrenheit, '.2f')}°F")

## ============================================
## EX2B - LAB 3: TAXES (taxes.py)
## ============================================

salary = 5000
tax_rate = 0.23
tax_withheld = salary * tax_rate

print(f"Your monthly salary is ${format(salary, '.2f')}")
print(f"Federal taxes withheld (23%) are ${format(tax_withheld, '.2f')}")
print(f"Your take home pay is ${format(salary - tax_withheld, '.2f')}")

## ============================================
## EX2B - LAB 4: DISTANCE (distance.py)
## ============================================

import math

x1, y1 = 1, 2
x2, y2 = 7, 10

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {format(distance, '.2f')}")

## ============================================
## EX2B - LAB 5: TILES (tiles.py)
## ============================================

length = 12
width = 10
tiles_per_box = 12
extra = 0.10

total_tiles_needed = length * width
tiles_with_extra = total_tiles_needed * (1 + extra)
boxes_needed = math.ceil(tiles_with_extra / tiles_per_box)  # round UP, cant buy partial box

print(f"Room size: {length} x {width} feet")
print(f"Tiles needed (with 10% extra): {math.ceil(tiles_with_extra)}")
print(f"Total boxes to buy: {boxes_needed}")

## ============================================
## EX2B - LAB 6: RENTALS (rentals.py)
## ============================================

tourists = 38
seats_per_van = 15
van_cost_per_day = 250

vans_needed = math.ceil(tourists / seats_per_van)   # round UP, cant have partial van
total_van_cost = vans_needed * van_cost_per_day
cost_per_person = math.ceil(total_van_cost / tourists * 100) / 100  # round UP per person

print(f"Number of tourists: {tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${format(total_van_cost, '.2f')}")
print(f"Cost per person: ${format(cost_per_person, '.2f')}")

# ---- Check the math ----
total_collected = cost_per_person * tourists
leftover = total_collected - total_van_cost

print(f"\n-- Checking the math --")
print(f"Total collected: ${format(total_collected, '.2f')}")
print(f"Total van cost: ${format(total_van_cost, '.2f')}")
print(f"Leftover money: ${format(leftover, '.2f')}")
# Leftover exists because we rounded UP the cost per person
# so each person paid slightly more than the exact split
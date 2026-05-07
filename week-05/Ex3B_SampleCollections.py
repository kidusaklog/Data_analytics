# ╔══════════════════════════════════════════╗
# ║         KIDUS TESEMA                     ║
# ║    ~ Year Up United Student ~            ║
# ║       Data Analytics Track              ║
# ╚══════════════════════════════════════════╝

# Author: Kidus Tesema

## ============================================
## EXERCISE 3.A - LAB 1: NUMERIC CONVERSIONS
## ============================================

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# int(a)        # Error: ValueError - can't convert float string directly
int(b)          # works! gives 55
# int(c)        # Error: ValueError - letters in string
# int(d)        # Error: ValueError - letters in string

float(a)        # works! gives 101.1
float(b)        # works! gives 55.0
# float(c)      # Error: ValueError - letters in string
# float(d)      # Error: ValueError - letters in string

int(float(a))   # works! gives 101

a_sliced = int(float(a))
b_sliced = int(b)
c_sliced = int(c[:3])
d_sliced = int(d[7:])

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print(a.strip())
print(d.strip())

## ============================================
## EXERCISE 3.A - LAB 2: STRING CLEANING
## ============================================

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print(name_1.title())
print(name_2.title())
print(name_3.title())

print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))
# still strings! need to remove "," and cast as int to do math

salary_1_clean = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_clean, type(salary_1_clean))

## ============================================
## EXERCISE 3.B - LAB 1: MOVIE LIST
## ============================================

movie_list = ["Inception", "The Lion King", "Interstellar", "Black Panther", "Soul"]

print(f"The list movie_list includes my top {len(movie_list)} favorite movies")
print(movie_list)

print(sorted(movie_list))   # does NOT change the original list
print(movie_list)           # still in original order

movie_list.sort()           # CHANGES the original list permanently
print(movie_list)

movie_list.append("Coco")
print(movie_list)
print(f"The list movie_list now includes my top {len(movie_list)} favorite movies")

## ============================================
## EXERCISE 3.B - LAB 2: CANDY STORE
## ============================================

candy_types = ("Skittles", "Starburst", "Jolly Ranchers")
fruity_flavors = ("Mango", "Watermelon", "Strawberry")

candy_combos = {
    candy_types[0] + " " + fruity_flavors[1],
    candy_types[1] + " " + fruity_flavors[0],
    candy_types[2] + " " + fruity_flavors[2],
}

print("Today's candy options include:")
print(candy_combos)
# sets are UNORDERED so the order changes every time you run it!

## ============================================
## EXERCISE 3.B - LAB 3: ADDRESS DICTIONARY
## ============================================

contact_info = {
    "name": "Kidus Tesema",
    "address": "123 Main St",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
}

print(f"{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

del contact_info["name"]

full_name = {
    "first name": "Kidus",
    "last name": "Tesema"
}

full_name.update({"honorific": "Mr."})

contact_info.update({"full_name": full_name})

print(f"{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")
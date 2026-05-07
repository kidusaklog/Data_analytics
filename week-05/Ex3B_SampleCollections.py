# ╔══════════════════════════════════════════╗
# ║         KIDUS TESEMA                     ║
# ║    ~ Year Up United Student ~            ║
# ║       Data Analytics Track              ║
# ╚══════════════════════════════════════════╝

# Author: Kidus Tesema

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

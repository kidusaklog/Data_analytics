f = open("about_me.txt", "r")
print(f.read())
f.close()


f = open("about_me.txt", "r")
print(f.read(50))   
print(f.read(50))   
f.close()

# ─────────────────────────────────────────
# Step 13 - readline()
f = open("about_me.txt", "r")
print(f.readline(10))  # "Name: Kidu"
print(f.readline())    # "s\n" (rest of line 1)

for i in range(1, 5):
    print(f.readline())  # prints lines 2, 3, 4, 5
f.close()

# ─────────────────────────────────────────
# Step 14 - readlines()
f = open("about_me.txt", "r")
print(f.readlines())       # entire file as list
print(f.readlines(1))      # ['Name: Kidus\n']
print(f.readlines(10))     # first ~10 chars worth of lines
print(f.readlines(100))    # first ~100 chars worth of lines
print(f.readlines(-1))     # all remaining lines
f.close()

# ─────────────────────────────────────────
# Step 15 & 16 - Combining all three methods
f = open("about_me.txt", "r")

first_50 = f.read(50)

next_four_lines = []
for i in range(1, 5):
    next_four_lines.append(f.readline())

next_100 = f.readlines(100)

f.close()

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")
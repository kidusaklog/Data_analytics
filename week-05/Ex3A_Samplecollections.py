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

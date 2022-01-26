name = input("What is your name?")

if name == "":
    print("Please enter your name")
else:
    print("Welcome to "+name)

print("\n")

month = input("Enter your Month")
if month == "January":
    print("You are in term 1")
elif month == "May":
    print("You are in term 2")
elif month == "September":
    print("You are in term 3")
else:
    print("You are in month where no term begins")

print("\n")
# No Switch/case statement = https://www.python.org/dev/peps/pep-3103/
print("Use Dictionaries")
term_month_map = {"January":"Term1", "May": "Term2", "September":"Term3"}
print("You are in "+term_month_map.get(month,"month where no term begins"))

print("\n")
print("Try except")
# print("You are in "+term_month_map[month])

try:
    print("You are in "+term_month_map[month])
except:
    print("You are in month where no term begins")
else:
    print("Good value")
finally:
    print("You are done!")


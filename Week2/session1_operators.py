print("***** Comparison Operators *****")
int_value1 = 10
int_value2 = 5
value_eg = 257

str_value1 = "Python"
str_value2 = "Django"

print("=== Integers comparison ===")
print(int_value1 == 20)
print(int_value2 == 10)
print("\n")

print(int_value1 != 10)
print(int_value2 != 10)
print("\n")

print(int_value1 < 10)
print(int_value2 >= 5)
print("\n")

print(int_value1 < int_value2)
print(int_value1 > int_value2)
print("\n")

print("=== String comparison ===")
print(str_value1 == "Python")
print(str_value2 != "Django")
print("\n")

# value comparison vs object comparison to be discussed later
# For people having background on class/objects, explore and discuss in chat in free time
"""print("Advanced topic 'is' vs '=='")
list1 = []
list2 = []
print(list1 is list2)
print("\n")"""

print("***** Logical Operators *****")
print("=== AND ===")
print(True and False)
print(True and True)
print(False and True)
print(False and False)
print("\n")

print("=== OR ===")
print(True or False)
print(True or True)
print(False or True)
print(False or False)
print("\n")

print("Example with variables")
print((int_value1 > int_value2) and (str_value1 == "Python"))
print("\n")

print("=== NOT ===")
print(not True)
print(int_value1 > int_value2)
print(not(int_value1 > int_value2))



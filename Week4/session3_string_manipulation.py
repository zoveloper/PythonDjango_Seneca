my_string = "Creativity is intelligence having fun!"

print(my_string[0:5] + my_string[-8:-5] + " " + my_string[11:13] + my_string[-5:-1])

print(my_string.find("intelligence"))

print(my_string.replace("intelligence", "intellect"))

#value = input("Enter the language")
value = "python"

if value == "PYTHON":
    print("Good, you can proceed")
else:
    print("Improper language for the class")

my_string = "random string"
print(my_string.capitalize())

my_string = "RANDOM string"
print(my_string.lower())

my_string = "random string"
print(my_string.upper())

my_string = "random string"
print(my_string.title())

my_string = "    random string    "
print(my_string.strip())

alpha = "abcdefg"
lowercase = "a lowercase string"
digits = "0123456789"
print(alpha.isalpha()) # returns True
print(lowercase.isalpha()) # returns False
print(digits.isalpha()) # returns False

digits = "0123456789"
lowercase = "a lowercase string"
print(digits.isdigit()) # returns True
print(lowercase.isdigit()) # returns False

space = "   "
print(space.isspace()) # returns True
 
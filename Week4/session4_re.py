import re

quote = "There is no terror in the bang, only in the anticipation of it! \
- Alfred Hitchcock"

# Escape Character "\"
#print("gonna "quote" here")

# Best place to explore 're' is at https://www.w3schools.com/python/python_regex.asp
new_quote = re.sub(r"([,!])", "....", quote)
print(new_quote)

match_obj = re.search("^There", quote)
print(match_obj)

print(match_obj.span())
print(match_obj.string)
print(match_obj.group())

print(re.search("^What", quote))

quote_words = re.split("\s", quote)
print(quote_words)

my_string = "Knowledge987is4565the3453most647democratic56786source2342of123power"

remove_digits = re.split("\d+", my_string)
print(remove_digits)

new_quote = " ".join(remove_digits)
print(new_quote)
# You can use single, double, or trible quotes for strings

my_string = "A double-quoted string"
your_string = 'A single quoted string'

multiline_string = '''This is my string that
                      goes on multiple lines
                      for whatever reason'''

# You can CONCATINATE strings with plus operators

little_string = "bad"
medium_string = "super"
long_string = medium_string + little_string
print(long_string)
# prints: superbad

""" 
You might recall using string template literals in JavaScript, 
which allow embedding expressions in strings using backticks and ${}.

Python’s approach is similar but has a key difference: 
you must prefix the string with an f to indicate it’s an f-string (formatted string literal).
"""

state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
print(message)
# prints: Hawaii was the last state to join the U.S. in 1959.

""" USEFUL STRING METHODS """

print("ace of spades".split(" "))
# prints: ['ace', 'of', 'spades']

# however, this won't work:
print("abcd".split(""))
# ValueError: empty separator

# instead, use the list() function like this:
print(list("abcd"))
# prints: ['a', 'b', 'c', 'd']

# get the index of a substring:
print("abcd".index("c"))    
# prints: 2
# this method raises an error if the substring is not found:
print("abcd".index("e"))
# ValueError: substring not found

# .find() is similar to .index() but returns -1 if the substring is not found
# this behavior may be preferable to raising an error:
print("abcd".find("e"))
# prints: -1

print("boo".upper())
# prints: 'BOO'

print("WHY???".lower())
# prints: 'why???'

print("Then I went to the store I like".replace("I", "you"))
# prints: 'Then you went to the store you like'

""" Want to know if a string contains a substring? You don’t even need a method for that! You can use the in operator to quickly find out if one string appears in another. """

print("eggs" in "green eggs and ham")
# prints: True

# Length 

print(len("Tacos"))
# prints: 5

# https://docs.python.org/3/library/stdtypes.html#string-methods
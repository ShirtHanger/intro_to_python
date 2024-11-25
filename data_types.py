# We use the type() function to obtain the datatype:

print(type("hello"))
# prints: <class 'str'>

# Strings are words 

print(type(25))
# prints: <class 'int'>

# Integers are FULL numbers

print(type(3.14159))
# prints: <class 'float'>

# Floats are DECIMAL numbers... this will create some hurdles in number logic

print(type(25.))
# Still a float

# Booleans are capitalized in python

print(type(True))
# prints: <class 'bool'>

# print(type(true))
# NameError: name 'true' is not defined. Did you mean: 'True'?

print(type(None))
# prints: `<class 'NoneType'>`

# Similar to null in JavaScript.

""" DATA TYPE CONVERSION """

# Python cannot convert datatypes automaticaly

""" 
num_tacos = 25
msg = "There are " + num_tacos + " tacos."
# TypeError: can only concatenate str (not "int") to str

"""

# You can solve this with commas, or direct conversions

# str(item)        # Converts `item` to a string
# int(item, base)  # Converts `item` to an integer with the provided `base`
# float(item)      # Converts `item` to a floating-point number
# hex(int)         # Converts `int` to a hexadecimal string
# oct(int)         # Converts `int` to an octal string
# tuple(item)      # Converts `item` to a tuple
# list(item)       # Converts `item` to a list
# dict(item)       # Converts `item` to a dictionary

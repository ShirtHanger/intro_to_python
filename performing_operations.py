""" 
Python has the normal math operators that you are used to from JavaScript:

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modulo (remainder) (%)
Exponentiation (**)
All work as you would expect. However, there are a few special operations worth mentioning.
"""

# The result of any division operaiton is a float, even if both numbers are integers

result = 4 / 2
print(result)
# prints: 2.0
print(type(result))
# prints: <class 'float'>

# Double slashes will fix this
result = 4 // 2
print(result)
# prints: 2 because the decimal ".0" is truncated

# Using = after an operator is a SHORTCUT, and will let you quickly updatw a variable

num = 0

# this line of code:
num = num + 1
# can be written with this shortcut operator:
num += 1

# it also works for any of the other math operations:
num = num / 5
# can be rewritten like this:
num /= 5

# and this line:
num = num * 3
# can be written as this:
num *= 3
# and so on with the other operators
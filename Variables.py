"""Variables"""

var = 1
print(var)

Import = "invalid syntax would be for \"import\" variable"
print(Import)

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name, sep=" ; ")
print(var)

var = "3.8.5"
print("Python version: " + var)

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# i = i + 2 * j ⇒ i += 2 * j
# var = var / 2 ⇒ var /= 2
# rem = rem % 10 ⇒ rem %= 10
# j = j - (i + var + rem) ⇒ j -= (i + var + rem)
# x = x ** 2 ⇒ x **= 2

kilometers = 12.25
miles = 7.38
#1 mile is equal to approximately 1.61 kilometers
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

a = 6
b = 3
a /= 2 * b
print(a)
# 2 * b = 6
# a = 6 → 6 / 6 = 1.0

"""Key takeaways
1. The name of the variable must be composed of upper-case or lower-case letters, digits, and the underscone character ( _ ).
2. The name of the variable must begin with a letter.
3. The underscore character is a letter.
4. Keywords cannot be used for the variable:
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
5. Python is a dynamically-typed language var = 1.
"""
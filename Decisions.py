"""Decisions"""

a = 1
b = 2
a == b #compares a and b
print(a==b)

"""
Priority	Operator	
1	        +, -	        unary
2	        **	
3	        *, /, //, %	
4	        +, -	        binary
5	        <, <=, >, >=	
6	        ==, !=
"""

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
# Print the result
print("The larger number is:", larger_number)


# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2
# Print the result
print("The larger number is:", larger_number)


# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1
# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2
# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3
# Print the result
print("The largest number is:", largest_number)


# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
largest_number = max(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)


name = input("Enter flower name: ")
if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")



x = "1"
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
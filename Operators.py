"""Operators"""

print("Python operators: +, -, *, /, //, %, ** ")
print(2+3) #add operator

print(2**2) #exponentiation (power) operator
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3) #multiplication (asterisk) operator
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3) #divisional (slash) operator
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
"""The result produced by the division operator is always a float ( 2.0 ; 3,0 ; 4,5 ; etc.....)"""
print(6 // 3) #integer (double slash) divisional
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(14 % 4) #modulo (remainder left after the integer division)

print(-4 + 4) #addition operator
print(-4. + 8)

print(-4 - 4) #subtraction operator
print(4. - 8)

print(-1.1) #minus operator
print(+2) #plus operator

print (2+3*5) #the hierarchy of priorities ( 3 * 5 ...  + 2 = ...)

print(2 ** 2 ** 3) 
"""the exponentiation operator uses right-sided binding 
2 ** 2 → 4; 4 ** 3 → 64
2 ** 3 → 8; 2 ** 8 → 256
"""

"""
Priority	Operator	
1	**	
2	+, - (note: unary operators located next to the right of the power operator bind more strongly)	unary
3	*, /, //, %	
4	+, -
Order from the highest (1) to the lowest (4) priorities.
"""

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) #subexpressions in parentheses are always calculated first

"""Key takeaways
1. An expression is a combination of values (or variables, operators, calls to functions ‒ you will learn about them soon) which evaluates to a certain value, e.g., 1 + 2.

2. Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the * operator multiplies two values: x * y.

3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division ‒ always returns a float), % (modulus ‒ divides left operand by right operand and returns the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation ‒ left operand raised to the power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division ‒ returns a number resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)

4. A unary operator is an operator with only one operand, e.g., -1, or +3.

5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

6. Some operators act before others – the hierarchy of priorities:

the ** operator (exponentiation) has the highest priority;
then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example: 4 ** -1 equals 0.25)
then *, /, //, and %;
and, finally, the lowest priority: the binary + and -.
7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.
"""
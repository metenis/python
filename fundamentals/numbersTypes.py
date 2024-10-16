# Integers (int) - whole numbers, e.g. 1, 2, 3, etc.
x = 1  # assign an integer value to variable x
print(x)  # output: 1

# Floating Point Numbers (float) - decimal numbers, e.g. 3.14, -0.5, etc.
y = 3.14  # assign a float value to variable y
print(y)  # output: 3.14

# Complex Numbers (complex) - numbers with real and imaginary parts, e.g. 3+4j, 2-5j, etc.
z = 3 + 4j  # assign a complex value to variable z
print(z)  # output: (3+4j)

# Boolean Values (bool) - true or false values
is_admin = True  # assign a boolean value to variable is_admin
print(is_admin)  # output: True

# Note: In Python, Boolean values are a subtype of integers, where True is equivalent to 1 and False is equivalent to 0.

# Long Integers (long) - long integers, e.g. 12345678901234567890, etc. (only in Python 2.x)
# Note: In Python 3.x, the long type is merged with int, so we don't need to use long explicitly.

# Decimal Values (decimal) - decimal numbers with arbitrary precision, e.g. Decimal('3.14'), etc.
from decimal import Decimal  # import the Decimal module
d = Decimal('3.14')  # create a Decimal object
print(d)  # output: 3.14

# Fraction Values (fractions) - rational numbers, e.g. Fraction(1, 2), etc.
from fractions import Fraction  # import the Fraction module
f = Fraction(1, 2)  # create a Fraction object
print(f)  # output: 1/2
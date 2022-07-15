# Examples for Arithmetic Operators

# Lets assign some values to variables
a = 13
b = 5
## a, b = 13, 5

# Addition Operator
c = a + b
print("Addition of 'a' and 'b' is: ", c)
print("This is the identity of c: ", id(c))
print("Addition of 'a' and 'b' is: ", a + b)
print("This is the identity of a+b: ", id(a + b))

# Subtraction Operator
c = a - b
print("Subtraction of 'a' and 'b' is: ", c)
print(id(c))
print("Subtraction of 'a' and 'b' is: ", a - b)
print(id(a - b))

# Multiplication Operator
c = a * b
print("Multiplication of 'a' and 'b' is: ", c)
print(id(c))
print("Multiplication of 'a' and 'b' is: ", a * b)
print(id(a * b))

# Division Operator
c = a / b
print("Division of 'a' and 'b' is: ", c)
print(id(c))
print("Division of 'a' by 'b' is: ", a / b)
print(id(a / b))

# Modulus Operator
print("The value of a: ", a)
print("The value of b: ", b)
print("Modulus of 'a' by 'b' gives remainder: ", b % a)

# Exponent Operator
print("The value of a: ", a)
print("The value of b: ", b)
print("Exponent of 'a' to the power of 'b' is: ", a ** b)

# Integer Division Operator
print("The value of a: ", a)
print("The value of b: ", b)
print("Integer Division of 'a' by 'b' gives integer value of quotient: ", a // b)

# Order of Evaluation
x = 1; y = 2; z = 3; a = 2; b = 2; c = 3
result = (x + y) * z ** a // b + c
print("The answer for order of evaluation is: ", result) 

# Example for Assignment Operator

## x = 20
## y = 10
## z = 5

# Different assigning methods
## x, y, z = 20, 10, 5

### Addition Assignment Operator

x, y, z = 20, 10, 5
print("x: ", x)
print("x identity: ", id(x))
print("y: ", y)
print("y identity: ", id(y))
print("z: ", z)
print("z identity: ", id(z))
print()
z += x
print("z identity: ", id(z))
print("Will add x and z and will store its result in z: ", z)

# Subtraction Assignment Operator
x, y, z = 20, 10, 5
z -= x
print("Will subtract z from x and will store its result in z: ", z)

# Multiplication Assignment Operator
x, y, z = 20, 10, 5
z *= x
print("Will multiply x with z and will store its result in z: ", z)

# Division Assignment Operator
x, y, z = 20, 10, 5
z /= x
print("Will divide z by x and will store its result in z: ", z)

# Modulus Assignment Operator
x, y, z = 20, 10, 5
z %= x
print("Will divide z by x and will store its result in z: ", z)

# Exponential Assignment Operator
x, y, z = 20, 10, 5
z **= y
print("Will perform power value of x for z and will store its result in z: ", z)

# Floor Division Assignment Operator
x, y, z = 20, 10, 5
z //= y
print("Will perform floor division and will store its result in z: ", z)

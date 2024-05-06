int
float
complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# casting in python they used change one data type to another
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8

# bitwise operater

x = 12
y = 5
result = x & y  # 1100 & 0101 = 0100 (decimal 4)
print(f"Result of x & y: {result}")

print("result is:",result)

x = 12
y = 5
result = x | y  # 1100 | 0101 = 1101 (decimal 13)
print(f"Result of x | y: {result}")


x = 12
result = ~x  # ~1100 = 0011 (decimal -13)
print(f"Result of ~x: {result}")


x = 12
y = 5
result = x ^ y  # 1100 ^ 0101 = 1001 (decimal 9)
print(f"Result of x ^ y: {result}")

x = 12
result = x << 2  # 1100 << 2 = 110000 (decimal 48)
print(f"Result of x << 2: {result}")

x = 12
result = x >> 1  # 1100 >> 1 = 0110 (decimal 6)
print(f"Result of x >> 1: {result}")


x=10
y=11
print( x==y)
a=True
print(not a)


# Arithmetic
a = 7
b = 2

print('Sum:', a + b)               # Addition
print('Subtraction:', a - b)       # Subtraction
print('Multiplication:', a * b)    # Multiplication
print('Division:', a / b)          # Division
print('Floor Division:', a // b)   # Floor Division
print('Modulo:', a % b)            # Modulo
print('Power:', a ** b)            # a to the power b



# 2. assignment



a = 6
b = 5
c = a + b  


a = 4
b = 5
a += b  

a = 6
b = 5
a -= b  


a = 4
b = 5
a *= b  

a = 3
b = 5
a /= b  

a = 10
b = 3
a %= b  

# comparation

a=15
b=6

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

# logical operater

a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")
else:
    print("At least one number is not greater than 0")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")


x = True

if not x:
    print("The boolean value is False")
else:
    print("The boolean value is True")


# membership operater  and identify

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  

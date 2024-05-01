'''

type of variable

int 
float
boolean,
string 
list,
tuple,
set 
dicternary
double
 '''

a=20
print(type(a))


#type convertion
x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
'''



# Variable Names

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
_kamal5="123"

# Example
# Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:



# 1.Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"


# 2.Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# 3.Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"

'''
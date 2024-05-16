x="tutor joes"

print(x)
print(type(x))
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
print(x.count("t"))
print(x.endswith("es"))
print(x.endswith("ES"))
print(x.find("o"))
print(x.find("o",5))
print(x.replace("o","*"))
print("***********************")


a="joes12347"
# # isalnum()	Returns True if all characters in the string are alphanumeric
# print(a.isalnum())
# # isalpha()	Returns True if all characters in the string are in the alphabet
# print(a.isalpha())

# isascii()	Returns True if all characters in the string are ascii characters
print(("ascii",a.isascii()))
# isdecimal()	Returns True if all characters in the string are decimals
print(a.isdecimal())
# isdigit()	Returns True if all characters in the string are digits
print(a.isdigit())
# isidentifier()	Returns True if the string is an identifier
print(a.isidentifier())
# islower()	Returns True if all characters in the string are lower case
print(a.islower())
# isnumeric()	Returns True if all characters in the string are numeric
print(a.isnumeric())
# isprintable()	Returns True if all characters in the string are printable
print(a.isprintable())
# isspace()	Returns True if all characters in the string are whitespaces
print(a.isspace())
# istitle()	Returns True if the string follows the rules of a title
print(a.istitle())
# isupper()	Returns True if all characters in the string are upper case
print(a.isupper())
# join()	Joins the elements of an iterable to the end of the string
print(a.join("xyz"))


print("**********")
s="he\n is\n line"
print(s)
# split()	Splits the string at the specified separator, and returns a list
print(s.split(" "))
# splitlines()	Splits the string at line breaks and returns a list

print(s.splitlines())


print("--------------")
#slicing 
    # 0 1 2 3 4 5 6  7 8 9 10 11
    # -4 -3 -2 -1
b = "Hello, World!"
print(b[2:])

print(b[::])

print(b[2:6:2])

print(len(b))

print(b[-5:-2])

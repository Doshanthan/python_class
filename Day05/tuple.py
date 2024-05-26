# Python Tuples


thistuple = ("apple", "banana", "cherry")
print(thistuple)

'''
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Ordered
When we say that tuples are ordered, it means that the items have a defined order,
and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the
tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:


'''
tuple1 = ("abc", 34, True, 40, "male")
#NOT a tuple
# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.

#ex1
thistuple = ("apple",)
print(type(thistuple))

#ex2
thistuple = ("apple")
print(type(thistuple))


# update the element first change datatype list after that change value..
#tuple datatype not change it is muttable
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#loop example of the tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



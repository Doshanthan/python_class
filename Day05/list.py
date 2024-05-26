#python list 
'''
mylist = ["apple", "banana", "cherry"]
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

1.Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

2.Allow Duplicates
Since lists are indexed, lists can have items with the same value:
3.
Lists allow duplicate values:'''

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


a = ["abc", 34, True, 40, "male"]
print(type(a))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))




'''List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''


#01......slicing python example

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  


#02........ add the new element in the list(0-error ,1-correct)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#0
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# 03..........Insert Items
'''
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index

'''


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# 4..........Append Items
'''
To add an item to the end of the list, use the append() method:

Using the append() method to append an item last index to used
'''

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# 5............Extend List
# To append elements from another list to the current list to extend method is used

thislist = ["apple", "banana", "mango"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# 6.........Remove Specified Item
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# 7..........Remove Specified Index
# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# 7.............del
# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# 8..........Clear the List
# The clear() method empties the list.


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# there are some method list
'''
append()	Adds an element at the end of the list
clear()     Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''
"""
In this exercise, you should find a list **method** that will combine two lists.

We have used the append function so far to append items to the end of a list.
Use the `dir()` function on lists and/or consult the Python documentation (https://docs.python.org/3/tutorial/datastructures.html)
to find a 
suitable list method that allows you to combine the two lists.
*Note* - You should find a single list method that is not append. 
It is possible to make the test pass using append, but that solution will not be counted as correct.
You need to find another list method.

For the two lists below, you should combine list1 and list2 
so that the result is [1, 2, 3, 4, 5, 6].

Ensure the `list1` retains its original object ID after combining the lists.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Get the id of the first list
id1 = id(list1)

# Write code here to combine list1 and list2. 
# The updated list should be stored in the variable name
# list1 and the ID should not be changed.

# Get the id of the list again
id2 = id(list1)

# Don't modify these lines. This is for testing.
assert id1 == id2
assert list1 == [1,2,3,4,5,6]

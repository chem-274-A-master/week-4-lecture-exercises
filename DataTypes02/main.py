"""
In this exercise, you should write a function called `combine_lists` that takes two lists as input 
and combines the second list into the first list.

You should use a single list method (not `append`) to combine the lists.

Requirements:
- The function should modify the first list in place (i.e., the ID of the first list should not change).
- After combining, the first list should contain all elements from both lists.
- Return the combined list from the function.

Example:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combine_lists(list1, list2) should return [1, 2, 3, 4, 5, 6]

"""

def combine_lists(list1, list2):
    """
    Combine list2 into list1 without changing the ID of list1.
    """
    
    # Write your code here
    # it should be a single line of code

    
    return list1


# sample code
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# id before function
id1 = id(list1)

combined_list = combine_lists(list1, list2)

# id after the function
id2 = id(list1)

# when you print the ids, they should be the same
print(f"{id1} == {id2}")

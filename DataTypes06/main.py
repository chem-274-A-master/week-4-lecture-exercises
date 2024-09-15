"""
Dictionary Creation Exercise

Write a function called `create_dict` that takes two lists as input:
- `keys`: a list of keys (strings or other hashable types)
- `values`: a list of corresponding values

The function should return a dictionary where each key in the `keys` list is mapped to its corresponding value in the `values` list.
If keys and values are not the same length, the function should raise a `ValueError`.

Example:
    keys = ["CH4", "C2H6", "C3H8", "C2H6O"]
    values = [16.04, 30.07, 44.1, 46.07]
    create_dict(keys, values) should return:
    {"CH4": 16.04, "C2H6": 30.07, "C3H8": 44.1, "C2H6O": 46.07}

Your function should handle the case where the lengths of the two lists are unequal by raising a `ValueError`.

Write your function below:
"""

def create_dict(keys, values):
    pass

# Example usage:
keys = ["CH4", "C2H6", "C3H8", "C2H6O"]
values = [16.04, 30.07, 44.1, 46.07]

# This should return {"CH4": 16.04, "C2H6": 30.07, "C3H8": 44.1, "C2H6O": 46.07}
print(create_dict(keys, values))

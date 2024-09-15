"""
Set Exercise

In this exercise, you will write a function called `find_common_elements` that takes in two sets, `set_A` and `set_B`, 
and returns the elements that exist in both sets.

You might find it useful to review set operations: https://en.wikipedia.org/wiki/Set_(mathematics)#Basic_operations.

Requirements:
- The function should return a set containing only the elements that are present in both `set_A` and `set_B`.
- The function should work with any sets of strings.
- If no common elements are found, the function should return an empty set.

Example:
    set_A = {"CH4", "H2O", "CO2"}
    set_B = {"CH4", "O2", "N2"}
    find_common_elements(set_A, set_B) should return {"CH4"}

Write your code below:
"""

def find_common_elements(set_A, set_B):
    pass  

# Example usage:
set_A = {"CH4", "CH3-CH=O", "CHCH", "COP1OCCCO1", "CC(C)(C)P(C(C)(C)C)C12C3C4C5C1[Fe]45321678C2(c3ccc(C(F)(F)F)cc3)C1(c1ccc(C(F)(F)F)cc1)C6(c1ccc(C(F)(F)F)cc1)C7(c1ccc(C(F)(F)F)cc1)C28c1ccc(C(F)(F)F)cc1",
        "c1ccc2c(c1)cc(P1C3CCCC1CCC3)c1ccccc12"}
set_B = {"CHCH", "COP1OCCCO1", "c1ccc2c(c1)cc(P1C3CCCC1CCC3)c1ccccc12", "CH4", "CC(C)N1CCN2CCN(C(C)C)P1N(C(C)C)CC2"}

# This should return {'COP1OCCCO1', 'c1ccc2c(c1)cc(P1C3CCCC1CCC3)c1ccccc12', 'CHCH', 'CH4'}
print(find_common_elements(set_A, set_B))

"""
Exercise: Object Introspection with Pickling

Objective:
    Use Python object introspection functions on a pickled object.

Background:
    - "Pickling" in Python refers to the process of serializing an object. This allows for the storage 
      and later retrieval of the object without having to re-execute its source code.
    - For this exercise, a Python object has been pickled and saved in this directory as 'object.pkl'.
      This object is loaded into a variable named 'obj'.

Tasks:
    1. Use a function you've learned to determine the data type of the `obj` variable. Print the output format as 
       'something', extracted from "<class 'something'>".
    2. Employ another introspection function to identify and print the name of any method within the `obj` 
       object that starts with the letter "c".
"""

import pickle

obj = pickle.load(open("object.pkl", "rb"))

# Task 1: Use an introspection function to determine the type of obj.
print("Your output here for task 1")

# Task 2: Use another introspection function to find a method in obj that begins with the letter "c".
print("Your output here for task 2")


import pickle

obj = pickle.load(open("object.pkl", "rb"))

# Print the type of obj. The data type will look like "<class 'something'>" write only what is in 'something' in the print statement.
print("")

# Print the name of the method in obj that begins with the letter "c".
print("")


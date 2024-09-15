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

import os
import pickle

# This makes sure the pickle file is read from the correct directory
# you can ignore this part
script_dir = os.path.dirname(os.path.realpath(__file__))
pickle_path = os.path.join(script_dir, "object.pkl")

with open(pickle_path, "rb") as f:
    obj = pickle.load(f)

# Task 1: Use an introspection function to determine the type of obj.
# Print your output in the format 'something', extracted from "<class 'something'>"
print("")

# Task 2: Use another introspection function to find a method in obj that begins with the letter "c".
print("")


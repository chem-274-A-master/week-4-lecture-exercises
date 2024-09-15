import inspect
import os
import sys
import subprocess

import pytest

def test_introspection01():
    # directory containing Introspection01 exercise
    script_dir = os.path.join(os.path.dirname(__file__), '..', 'Introspection01')

    script_path = os.path.join(script_dir, 'main.py')

    # run the script and capture the output
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    expected_type_output = "tuple"  # This is an example, change based on your object.pkl content
    expected_method_output = "count"  # Example for methods starting with "c"

    # Split the actual output from the script
    output_lines = result.stdout.strip().split("\n")

    # check the output from Task 1: The type of the object
    assert output_lines[0] == expected_type_output, f"Did not get the expected type, try again!"

    # check the output from Task 2: Method starting with "c"
    assert output_lines[1] == expected_method_output, f"Did not get the expected method, try again!"

def test_DataTypes01():

    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes01"))
    sys.path.append(exercise_dir)

    from main import floored_division

    # Define some test cases
    test_cases = [
        (10, 3, 3),       # Regular integer division
        (9, 2, 4),        # Integer division with no remainder
        (-10, 3, -4),     # Division involving negative numbers
        (5.3, 2.1, 2),    # Floored division with two floats
        (9, -4, -3),      # Negative denominator
        (0, 5, 0)         # Division by any number when numerator is zero
    ]


    for numerator, denominator, expected_result in test_cases:
        result = floored_division(numerator, denominator)
        assert result == expected_result, f"For {numerator} // {denominator}, expected {expected_result} but got {result}"

def test_DataTypes02():

    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes02"))
    sys.path.append(exercise_dir)

    # Import the function
    from main import combine_lists

    # Test case 1: Combine two integer lists
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    # Store the original id of list1
    id1 = id(list1)

    # Call the function
    result = combine_lists(list1, list2)

    # Check if the id of list1 is unchanged
    assert id(list1) == id1, "The ID of list1 should not change."
    
    # Check if the lists are combined correctly
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], but got {result}"

    # Test case 2: Combine with an empty list
    list1 = [7, 8]
    list2 = []

    # Store the original id of list1
    id1 = id(list1)

    # Call the function
    result = combine_lists(list1, list2)

    # Check if the id of list1 is unchanged
    assert id(list1) == id1, "The ID of list1 should not change."

    # Check if the lists are combined correctly
    assert result == [7, 8], f"Expected [7, 8], but got {result}"

def test_DataTypes03():

    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes03"))
    sys.path.append(exercise_dir)

    # Import the function
    from main import find_third_lowest_index

    numbers = (2.4600e02, 0.0000e00, 7.7100e01, 1.5690e02, -4.3680e02, 
               -3.3400e01, -1.1200e01, -4.0700e01, -9.6900e01, -1.0980e02, 
               -1.8700e02, -6.6200e01, 2.8940e02, 0.0000e00, -1.5823e03, 
               -1.4311e03)
    result = find_third_lowest_index(numbers)
    assert result == 4

def test_DataTypes04():

    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes04"))
    sys.path.append(exercise_dir)

     # Import the function
    from main import string_compare

    # Test case 1: Case insensitive comparison
    assert string_compare("energy", "Energy", case_sensitive=False), "Case insensitive comparison failed"

    # Test case 2: Case sensitive comparison
    assert not string_compare("energy", "Energy", case_sensitive=True), "Case sensitive comparison failed"

    # Test case 3: Case insensitive comparison with different strings
    assert not string_compare("energy", "Ch4", case_sensitive=False)

    # Two identical strings should return True  
    assert string_compare("energy", "energy")

def test_DataTypes05():
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes05"))
    sys.path.append(exercise_dir)

    # import the function
    from main import find_common_elements

    # Test case 1: Identical sets
    set_A = {"CH4", "H2O", "CO2"}
    set_B = {"CH4", "H2O", "CO2"}
    result = find_common_elements(set_A, set_B)
    assert result == {"CH4", "H2O", "CO2"}, f"Expected {{'CH4', 'H2O', 'CO2'}}, but got {result}"

    # Test case 2: Completely different sets
    set_A = {"CH4", "H2O", "CO2"}
    set_B = {"O2", "N2"}
    result = find_common_elements(set_A, set_B)
    assert result == set(), f"Expected empty set, but got {result}"

    # Test case 3: Partial overlap between sets
    set_A = {"CH4", "H2O", "CO2"}
    set_B = {"CH4", "N2", "O2"}
    result = find_common_elements(set_A, set_B)
    assert result == {"CH4"}, f"Expected {{'CH4'}}, but got {result}"

    # Test case 4: Empty set_A
    set_A = set()
    set_B = {"CH4", "CO2"}
    result = find_common_elements(set_A, set_B)
    assert result == set(), f"Expected empty set, but got {result}"

    # Test case 5: Empty set_B
    set_A = {"CH4", "CO2"}
    set_B = set()
    result = find_common_elements(set_A, set_B)
    assert result == set(), f"Expected empty set, but got {result}"

    # Test case 6: Both sets empty
    set_A = set()
    set_B = set()
    result = find_common_elements(set_A, set_B)
    assert result == set(), f"Expected empty set, but got {result}"

def test_DataTypes06():
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes06"))
    sys.path.append(exercise_dir)

    # import the function
    from main import create_dict

    # Test case 1: Standard case with molecule names and masses
    keys = ["CH4", "C2H6", "C3H8", "C2H6O"]
    values = [16.04, 30.07, 44.1, 46.07]
    result = create_dict(keys, values)
    expected = {"CH4": 16.04, "C2H6": 30.07, "C3H8": 44.1, "C2H6O": 46.07}
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Empty lists
    keys = []
    values = []
    result = create_dict(keys, values)
    expected = {}
    assert result == expected, f"Expected empty dictionary, but got {result}"

    # Test case 3: Unequal list lengths (should raise ValueError)
    keys = ["CH4", "C2H6", "C3H8"]
    values = [16.04, 30.07]
    with pytest.raises(ValueError):
        create_dict(keys, values)

    # Test case 4: Mixed data types
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    result = create_dict(keys, values)
    expected = {1: "one", 2: "two", 3: "three"}
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 5: Duplicate keys (last value should be used)
    keys = ["CH4", "C2H6", "C3H8", "CH4"]
    values = [16.04, 30.07, 44.1, 50.0]
    result = create_dict(keys, values)
    expected = {"CH4": 50.0, "C2H6": 30.07, "C3H8": 44.1}
    assert result == expected, f"Expected {expected}, but got {result}"


def test_DataTypes07():

    # Internal function to check if the function uses .items() by inspecting the source code
    def check_items_usage(func):
        # Get the source code of the function
        source_code = inspect.getsource(func)
        # Check if '.items()' is present in the source code
        return '.items()' in source_code

    # Add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DataTypes07"))
    sys.path.append(exercise_dir)

    # Import the function
    from main import find_gases

    # Test case 1: Standard case with hydrocarbons
    densities = {
      "methane": 0.0007,
      "ethane": 0.0013,
      "propane": 0.0019,
      "butane": 0.0025,
      "pentane": 0.626,
      "hexane": 0.659,
      "octane": 0.703,
      "decane": 0.73
    }
    result = find_gases(densities)
    expected = ['methane', 'ethane', 'propane', 'butane']
    assert result == expected, f"Expected {expected}, but got {result}"

    # Check if the function uses .items() by inspecting the source code
    assert check_items_usage(find_gases), "The function must use the .items() method to iterate through the dictionary"





"""
String Exercise

Strings have a number of built-in methods like .lower(), 
which converts a string to lowercase and .upper(), which converts a string to uppercase.

Sometimes when comparing strings, we do not want the capitalization to matter
(for example, 'Cat' should be considered equivalent to 'cat'). 
You can compare only letters in two strings by calling either .upper() or .lower() on both strings.

Write a function called `string_compare`. The function should take in two strings and return True if the two strings are the same. 
It should take an optional argument `case_sensitive` which should have the default value of False. 
If `case_sensitive` is True, the capitalization of the two strings should have to match.
"""

# Write your function here

if __name__ == "__main__":

  # Example usage

  # This should be True
  print(string_compare("energy", "Energy"))

  # This should be False
  print(string_compare("CH4", "Ch4", case_sensitive=True))
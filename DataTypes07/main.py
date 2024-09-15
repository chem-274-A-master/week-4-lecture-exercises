"""
Dictionary Iteration Exercise

Write a function called `find_gases` that takes a dictionary of substances and their densities as input and returns a list of substances that are gases.

Consider a substance to be a gas if its density is less than 0.1 g/mL.

For this exercise, you **must** use the `.items()` dictionary method to iterate through the dictionary.

Example:
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
    find_gases(densities) should return ['methane', 'ethane', 'propane', 'butane']

Write your function below:
"""

def find_gases(densities):
    pass

# Example usage:
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

# Expected: ['methane', 'ethane', 'propane', 'butane']
print(find_gases(densities))
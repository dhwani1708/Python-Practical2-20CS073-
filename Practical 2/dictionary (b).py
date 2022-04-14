# DHWANI SAKHIYA (20CS073)

# Write a Python script to merge two Python dictionaries.

def Merge(dict1, dict2):
    return (dict2.update(dict1))

# Driver code
dict1 = {'a': 10, 'b': 20}
dict2 = {'d': 30, 'c': 40}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)
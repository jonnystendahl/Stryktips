import numpy as np

# Two string arrays
array1 = np.array(['1', 'X', '2'])
array2 = np.array(['1', 'X', '2'])
array3 = np.array(['1', 'X', '2'])
array4 = np.array(['1', 'X', '2'])
array5 = np.array(['1', 'X', '2'])
array6 = np.array(['1', 'X', '2'])
array7 = np.array(['1', 'X', '2'])
array8 = np.array(['1', 'X', '2'])
array9 = np.array(['1', 'X', '2'])
array10 = np.array(['1', 'X', '2'])
array11 = np.array(['1', 'X', '2'])
array12 = np.array(['1', 'X', '2'])
array13 = np.array(['1', 'X', '2'])

# Create a meshgrid
meshgrid_result = np.meshgrid(array1, array2, array3, array4, array5, array6, array7, array8, array9, array10, array11, array12, array13)

# Combine the results into a single array of tuples
combinations = np.vstack([meshgrid_result[0].ravel(), meshgrid_result[1].ravel()]).T

# Concatenate strings from each tuple to create a 1D array of combinations
combinations_as_strings = np.core.defchararray.add(combinations[:, 0], combinations[:, 1])

# Display the result
print(combinations_as_strings)
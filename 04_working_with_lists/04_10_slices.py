# List comprehension to generate cubes of numbers from 1 to 10
cubes = [number ** 3 for number in range(1, 11)]

# Print the original list of cubes
print("List of cubes:", cubes)

# Print the first three items using a slice
print("The first three items in the list are:", cubes[:3])

# Print three items from the middle of the list using a slice
# Since the list has 10 elements, the middle items are at indices 3, 4, and 5
print("Three items from the middle of the list are:", cubes[3:6])

# Print the last three items using a slice
print("The last three items in the list are:", cubes[-3:])

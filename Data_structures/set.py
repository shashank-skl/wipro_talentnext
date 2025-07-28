# 1. Write a program to remove a given item from the set.
sample_set = {10, 20, 30, 40, 50}
item_to_remove = 30
sample_set.discard(item_to_remove)  # discard won't raise an error if item not found
print("Set after removing item:", sample_set)

# 2. Write a program to create an intersection of sets.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection_set = set_a & set_b  # or use set_a.intersection(set_b)
print("Intersection of sets:", intersection_set)

# 3. Write a program to create a union of sets.
set_x = {'apple', 'banana'}
set_y = {'banana', 'cherry'}
union_set = set_x | set_y  # or use set_x.union(set_y)
print("Union of sets:", union_set)

# 4. Write a program to find the maximum and minimum value in a set.
number_set = {15, 8, 22, 3, 41}
max_value = max(number_set)
min_value = min(number_set)
print("Maximum value in set:", max_value)
print("Minimum value in set:", min_value)

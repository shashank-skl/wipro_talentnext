# 1. Write a program to print the 4th element from the first and 4th element from the last in a tuple.
my_tuple = (5, 10, 15, 20, 25, 30, 35, 40)
if len(my_tuple) >= 4:
    print("4th element from start:", my_tuple[3])
    print("4th element from end:", my_tuple[-4])
else:
    print("Tuple has less than 4 elements.")

# 2. Write a program to check whether an element exists in a tuple or not.
check_tuple = (3, 6, 9, 12, 15)
element = 9
if element in check_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Write a program to convert a list into a tuple.
sample_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(sample_list)
print("Converted Tuple:", converted_tuple)

# 4. Write a program to find the index of an item in a tuple.
search_tuple = ('apple', 'banana', 'cherry', 'date')
item = 'cherry'
if item in search_tuple:
    index = search_tuple.index(item)
    print(f"Index of '{item}' is {index}.")
else:
    print(f"'{item}' not found in the tuple.")

# 5. Write a program to replace last value of tuples in a list to 100.
sample_list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list_of_tuples]
print("Updated list of tuples:", updated_list)

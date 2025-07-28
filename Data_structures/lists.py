# 1. Create a list of 5 integers and display the list items. Access individual elements through index.
numbers = [10, 20, 30, 40, 50]
print("Complete list:", numbers)
print("Accessing elements using index:")
print("First:", numbers[0])
print("Second:", numbers[1])
print("Third:", numbers[2])
print("Fourth:", numbers[3])
print("Fifth:", numbers[4])

# 2. Append a new item to the end of the list.
numbers.append(60)
print("After appending 60:", numbers)

# 3. Reverse the order of the items in the list.
numbers.reverse()
print("List after reversing:", numbers)

# 4. Print the number of occurrences of a specified element in a list.
element = 30
occurrences = numbers.count(element)
print(f"Number of times {element} appears in the list:", occurrences)

# 5. Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [7, 8, 9]
list2 = list1 + list2
print("list2 after adding list1 in front:", list2)

# 6. Insert a new item before the second element in an existing list.
list2.insert(1, 99)  # Insert 99 before the element at index 1
print("After inserting 99 before second element:", list2)

# 7. Remove the item from a specified index in a list.
del list2[3]  # Remove the element at index 3
print("After deleting item at index 3:", list2)

# 8. Remove the first occurrence of a specified element from a list.
list2.remove(2)  # Remove first occurrence of 2
print("After removing the first occurrence of 2:", list2)

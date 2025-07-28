#Q1. Write a program to check if a given number is Positive, Negative or Zero.
import math

number = int(input("Enter the numer"))
if(number>0):
    print(number + "is Positive")
elif(number<0):
    print(number + "is negative")
else:
    print("is Zero")


#Q2. Write a program to check if a given number is odd or even.
number = int(input("Enter the numer"))
if(number // 2 == 0):
    print("number is Even" )
elif(number // 2 != 0):
    print("Number is Odd")
else:
    print("Invalid number")


#Q3. # Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

number = int(input("Enter Desired Number"))
if(number//10 == 70):
    print(True)
else:False

#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
n = 10
for i in range(0, n):
    print(i)
    i+=1


#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

for i in range(23, 57, 2):
    print(i)



#Q6. Write a program to check if a given number is prime or not.
N= int(input("Enter a number"))
count = 0
for i in range(1, N):
    if(N%i == 0):
        count += 1
    if(count == 2):
        print("YES")
    else:
        print("Not a prime number")


#ANOTHER OPTIMAL APPROACH

N = int(input("Enter the number"))
M = math.sqrt(N)
for i in range(0, M):
    if(M % i == 0):
        count += 1
        if(M/ i != i):
            count += 1
if(count == 2):
    print("Pirme")
else: print("Not Prime")


# print prime numbers between 10 to 99
num = 10
while num <= 99:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
    if is_prime:
        print(num, end=' ')
    num += 1



#WAP to print sum of all Digits of a given number.
num = int(input("Enter the number"))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)




#WAP to reverse a given number and print
num = int(input("Enter the number"))
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10

print(reverse)

#WAP tto check if a number is Palindorme
num = str(input("Enter the number"))
if num[::-1] == num:
    print('palindrome')
else:
    print("Not a Palindorme")



#    -- DATA STRUCTURES --


#Create a dictionary that contains a list of people and one interesting fact about each of them.
#Display each person and his or her interesting fact on the screen.
#Next, change a fact about one of the people.
#Also, add an additional person and their corresponding fact.
#Display the new list of people and facts.
#Run the program multiple times and notice if the order changes.

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
print()

people_facts["Jeff"] = "Is afraid of heights."
people_facts["Jill"] = "Can hula dance."

print("Updated facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")



#Find the Runner-Up Score
#Project: 2

# Problem Statement:
#Given the participant’s score sheet for your University Sports Day, you are required to find the runner-up score.
#You have a list of scores. Your task is to:
#Store them in a list.
#Find and print the score of the runner-up (the second-highest score, not equal to the maximum if it appears more than once).


scores = [2, 3, 6, 6, 5]

max_score = max(scores)

scores = [score for score in scores if score != max_score]
runner_up = max(scores)
print(runner_up)



#Project: 3

# Problem Statement:
#You have a record of n students. Each record contains:
#The student’s name (string)
#Their percentage marks in Math, Physics, and Chemistry (as floating-point or integer values)
#You are required to:
#Save this data in a dictionary
#The student's name will be the ke
#The marks (as a list) will be the value
#The program should ask the user to enter a student’s name, and then output the average percentage marks obtained by that student.



student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

if name in student_marks:
    marks = student_marks[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {int(average)}")
else:
    print("Student not found.")


#Given a string of n words, help Alex to find out how many times his name appears in the string.
#Constraint: 1 <= n <= 200
#Sample input: Hi Alex WelcomeAlex Bye Alex.
#Sample output: 3
#Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.

name = str(input("Enter the String"))
count = 0
for word in name.split():
    if word == "Alex":
    count += 1
else:
    print("none found")

print (count)



#-- LIST --

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



#      ------------------------- DICTIONARY -------------------------------
# 1. Write a program to add a key and value to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}

sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated Dictionary:", sample_dict)

# 2. Write a program to concatenate the following dictionaries to create a new one.
# dic1 = {1: 10, 2: 20}, dic2 = {3: 30, 4: 40}, dic3 = {5: 50, 6: 60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
combined_dict = {}
for d in (dic1, dic2, dic3):
    combined_dict.update(d)
print("Concatenated Dictionary:", combined_dict)

# 3. Write a program to check if a given key already exists in a dictionary.

check_dict = {1: "apple", 2: "banana", 3: "cherry"}
key_to_check = 2
if key_to_check in check_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")

# 4. Write a program to iterate over a dictionary using for loop and print the keys alone,
# values alone, and both keys and values.

fruit_prices = {'apple': 60, 'banana': 30, 'cherry': 100}
print("Keys:")
for key in fruit_prices:
    print(key)

print("Values:")
for value in fruit_prices.values():
    print(value)

print("Key-Value Pairs:")
for key, value in fruit_prices.items():
    print(f"{key}: {value}")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are square of the keys.

squares_dict = {}
for i in range(1, 16):
    squares_dict[i] = i ** 2
print("Dictionary with squares of numbers 1 to 15:", squares_dict)

# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.

number_dict = {'a': 100, 'b': 200, 'c': 300}
total_sum = sum(number_dict.values())
print("Sum of all values:", total_sum)



#---------------------------------- TUPLE ----------------------------------

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




#----------------------- SET------------------------
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





 #---------------STRING----------------
# 1. Write a program to count the number of upper and lower case letters in a String.

def count_case_letters(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

count_case_letters("HelloWorld")

# -----------------------------------------------------

# 2. Write a program that will check whether a given String is Palindrome or not.

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

is_palindrome("Madam")
is_palindrome("Hello")

# -----------------------------------------------------

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.
# The string length will be >=2.
# Example: If input is "Wipro" then output should be "WiWiWiWiWi".

def repeat_first_two(s):
    if len(s) >= 2:
        front = s[:2]
        result = front * len(s)
        print(result)
    else:
        print("String must have at least 2 characters.")

repeat_first_two("Wipro")

# -----------------------------------------------------

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' characters, else return the string unchanged.
# If the input is "xHix", then output is "Hi".

def remove_x_ends(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    print(s)

remove_x_ends("xHix")
remove_x_ends("Hello")

# -----------------------------------------------------

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# You may assume that n is between 0 and the length of the string inclusive.
# Example: if the inputs are “Wipro” and 3, then the output should be “propropro”.

def repeat_last_n_chars(s, n):
    if 0 <= n <= len(s):
        end = s[-n:]
        result = end * n
        print(result)
    else:
        print("Invalid value for n.")

repeat_last_n_chars("Wipro", 3)









#1.	create a python program that asks the user how far they want to travel.
# if they want to travel less than three miles tell them to ride Bicycle.
# if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle.
# if they want to travel three hundred miles or more tell them to driver Super-Car.

asking_user = int(input("How far would you like pt travel in mies?"))
if(asking_user<=3):
    print("I suggest you to walk")

elif(300<asking_user>3):
    print("i sugget you to ride motor cycle")

else:
    print("I suggest super-car to your destination")







#2.	Let's assume you are planning to use your python skills to build an App for Mobile.
#You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
#Write a python program that displays the answers to the following questions:
#How much does it cost to operate one server per day?
#How much does it cost to operate one server per week?
#How much does it cost to operate one server per month?
#How much days can I operate one server with $918?

hourly_rate = 0.51

cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 918
days_with_budget = budget / cost_per_day
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month (30 days): ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for approximately {days_with_budget:.2f} days.")











#------------------------------------FUNCTIONS/MODULES/PACKAGES------------------------------

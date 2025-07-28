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

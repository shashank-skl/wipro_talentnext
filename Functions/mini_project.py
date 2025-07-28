# Project: 1
# Stream: Python
# Tech Module: Functions/Modules/Packages
#
# Problem Statement:
# Write a Python function that accepts a hyphen-separated sequence of colors as input
# and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
#
# Constraint:
# All the colors will be completely in either lower case or upper case.
#
# Sample Input 1: "green-red-yellow-black-white"
# Sample Output 1: "black-green-red-white-yellow"
#
# Sample Input 2: "PINK-BLUE-TAN-PURPLE"
# Sample Output 2: "BLUE-PINK-PURPLE-TAN"

def sort_colors_hyphen_separated(input_string):
    color_list = input_string.split('-')

    sorted_colors = sorted(color_list)

    return '-'.join(sorted_colors)


print(sort_colors_hyphen_separated("green-red-yellow-black-white"))  # Output: black-green-red-white-yellow
print(sort_colors_hyphen_separated("PINK-BLUE-TAN-PURPLE"))  # Output: BLUE-PINK-PURPLE-TAN


#-----------------------------------------------------------------------------------------------------

# Project: 2
# Stream: Python
# Tech Module: Functions/Modules/Packages
#
# Task:
# Create a Python module with the following functions:
# 1. ispalindrome(name) – Determines whether the provided name is a palindrome.
# 2. count_the_vowels(name) – Returns the number of vowels in the given name.
# 3. frequency_of_letters(name) – Returns the frequency count of each letter in the name.
#
# Note: The input name will be in either lowercase or uppercase.
# These functions should be saved in a module and tested from another script using appropriate inputs.

# Define all the functions in a Python module

def ispalindrome(name):
    reversed_name = name[::-1]
    return name == reversed_name

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != ' ':  # skip spaces
            freq[char] = freq.get(char, 0) + 1
    return freq

# 1. Write a function to return the sum of all numbers in a list.
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 2. Write a function to return the reverse of a string.
def reverse_string(text):
    return text[::-1]



# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
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



# 5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
def print_even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    print("Even numbers:", evens)


# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True




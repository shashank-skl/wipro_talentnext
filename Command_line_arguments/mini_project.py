# Write a program to accept two numbers as command line arguments and display their sum.

import sys

# Ensure exactly two arguments are passed (excluding the script name)
if len(sys.argv) != 3:
    print("Please provide exactly two numbers as command line arguments.")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        total = num1 + num2
        print("Sum:", total)
    except ValueError:
        print("Please enter valid integers.")




# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys

# Check if a message was passed
if len(sys.argv) < 2:
    print("Please provide a welcome message.")
else:
    filename = sys.argv[0]
    message = " ".join(sys.argv[1:])
    print(f"File Name: {filename}")
    print(f"Welcome Message: {message}")



# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys

# Check if exactly 10 numbers are provided
if len(sys.argv) != 11:
    print("Please provide exactly 10 numbers as command line arguments.")
else:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    try:
        numbers = list(map(int, sys.argv[1:]))
        prime_sum = sum(num for num in numbers if is_prime(num))
        print("Sum of prime numbers:", prime_sum)
    except ValueError:
        print("All inputs must be valid integers.")


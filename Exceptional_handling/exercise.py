# Write a program to accept two numbers from the user and perform division.
# If any exception occurs, print an error message or else print the result.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")




# Write a program to accept a number from the user and check whether it’s prime or not.
# If user enters anything other than number, handle the exception and print an error message.

try:
    num = int(input("Enter a number: "))
    if num < 2:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")




# Write a program to accept the file name to be opened from the user.
# If file exists, print the contents of the file in title case or else handle the exception.

try:
    file_name = input("Enter file name: ")
    with open(file_name, "r") as f:
        content = f.read()
        print("\nFile content in Title Case:\n")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:", str(e))




# Declare a list with 10 integers and ask the user to enter an index.
# Check whether the number in that index is positive or negative.
# If any invalid index is entered, handle the exception and print an error message.

nums = [12, -7, 0, 34, -56, 89, -32, 6, -1, 17]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = nums[index]
    if value > 0:
        print("The number at index", index, "is Positive.")
    elif value < 0:
        print("The number at index", index, "is Negative.")
    else:
        print("The number at index", index, "is Zero.")
except IndexError:
    print("Error: Index out of range. Please enter a value from 0 to 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")



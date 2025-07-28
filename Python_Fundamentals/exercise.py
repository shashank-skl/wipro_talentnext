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

# Write a program to read the entire content from a txt file and display it to the user.

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)


# Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter the number of lines to read: "))
with open("example.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())




# Write a program to accept input from user and append it to a txt file.

user_input = input("Enter text to append to the file: ")
with open("example.txt", "a") as file:
    file.write(user_input + "\n")
print("Text appended successfully.")




# Write a program to read contents from a txt file line by line and store each line into a list.

with open("example.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
print("Lines in list:", lines)



# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

with open("example.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)




# Write a program to count the frequency of a user entered word in a txt file.

search_word = input("Enter the word to search: ")
with open("example.txt", "r") as file:
    words = file.read().split()
    count = words.count(search_word)
print(f"The word '{search_word}' appears {count} times.")

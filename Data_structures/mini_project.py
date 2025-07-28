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


#------------------------------------------------------------------------------------------------------



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


#-----------------------------------------------------------------------------------------------------------

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


#-------------------------------------------------------------------------------------------------------------

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

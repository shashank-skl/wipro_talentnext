# Project 1: Final Happiness Calculator
# -----------------------------------------------------
# Through command line arguments, three strings separated by space are given.
# Each string is a sequence of numbers separated by hyphens (-).
# The first string contains numbers you like.
# The second string contains numbers you dislike.
# The third string contains numbers that are presented to you.
#
# You start with happiness = 0.
# For each number in the third string:
# - If it's in the like list (first string), add 1 to happiness.
# - If it's in the dislike list (second string), subtract 1 from happiness.
# - If it's not in either, happiness remains unchanged.
#
# Output the final happiness score.

def calculate_happiness(likes_str, dislikes_str, presented_str):
    # Convert hyphen-separated strings to sets and list
    likes = set(likes_str.split('-'))
    dislikes = set(dislikes_str.split('-'))
    presented = presented_str.split('-')

    happiness = 0

    for number in presented:
        if number in likes:
            happiness += 1
        elif number in dislikes:
            happiness -= 1

    return happiness


# Sample test run (you can replace these with sys.argv inputs for command-line usage)
# Example usage:
likes_input = "3-1"
dislikes_input = "5-7"
presented_input = "1-5-3-8"

result = calculate_happiness(likes_input, dislikes_input, presented_input)
print(result)  # Output: 1

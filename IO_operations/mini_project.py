# Project: Secret Message Decoder
# Problem:
# Your friend sends you a text file with hidden instructions to meet.
# The file contains 'n' lines of text.
# Rules:
# 1. The number of lines gives you the meeting time (in 12-hour format).
# 2. The most frequent word tells you the street name (add 'Street' to it).
# Task: Print the meeting time and meeting place.

from collections import Counter

def decode_meeting_details(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Count number of lines to determine meeting time
        num_lines = len(lines)
        hour = num_lines % 12
        if hour == 0:
            hour = 12
        meeting_time = f"{hour} {'AM' if num_lines <= 12 else 'PM'}"

        # Normalize and count all words
        words = []
        for line in lines:
            for word in line.strip().split():
                # Remove punctuation and convert to lowercase
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word:
                    words.append(clean_word)

        # Count frequency
        freq = Counter(words)
        most_common_word, _ = freq.most_common(1)[0]
        meeting_place = f"{most_common_word.capitalize()} Street"

        # Output
        print("Meeting time:", meeting_time)
        print("Meeting place:", meeting_place)

    except FileNotFoundError:
        print("File not found. Please check the filename.")

# Example usage:
# decode_meeting_details("Sample.txt")

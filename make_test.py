# David Bass
# Last updated 24 October 2022

# TODO
# Add command line arguments for specifying answer choice randomization and
# question point values.
# Add compatibility with alternate input formats, like noting correct answer
# choices by placing them first instead of placing an asterisk before them.

import sys
from string import ascii_lowercase

# Handle command line arguments
if len(sys.argv) < 3:
    raise "Two command line arguments (input file and output file) required."
input = sys.argv[1]
output = sys.argv[2]

# Read input file into "lines"
with open(input, "r") as f:
    lines = f.readlines()

# Read through input file
questions = {}
reading_question = True
for line in lines:
    # Remove whitespace from edges of line being read
    line = line.strip()

    # If line is blank, skip it and prepare to read in the next question
    if not line.strip():
        reading_question = True
        continue

    # Add new question key to "questions" dictionary
    if reading_question:
        question = line
        questions[question] = []
        reading_question = False
    # Add new answer choice as value to question key in "questions" dictionary
    else:
        questions[question].append(line)

# Write to output file
with open(output, "w") as f:
    # Iterate through questions
    for i, question in enumerate(questions.keys()):
        if question[0] == "=":
            f.write(str(i + 1) + ". (1 point)\n" + question[1:] + "\n")
            randomize_or_not = ""
        else:
            f.write(str(i + 1) + ". (1 point)\n" + question + "\n")
            randomize_or_not = "#randomize"

        # Write question to output file

        # Write answer choices to output file
        for j, answer in enumerate(questions[question]):
            if answer[0] == "*":
                f.write("*" + ascii_lowercase[j] + ". " + answer[1:] + "\n")
            else:
                f.write(ascii_lowercase[j] + ". " + answer + "\n")

        # Write keyword for randomizing answer choices, if first character of
        # question is not "=".
        f.write(randomize_or_not + "\n\n")




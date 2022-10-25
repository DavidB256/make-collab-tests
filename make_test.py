# David Bass
# Last updated 21 September 2022

# TODO
# Add command line arguments for specifying answer choice randomization and
# question point values
# Add compatibility with alternate input formats, like noting correct answer
# choices by placing them first instead of placing an asterisk before them.

import sys
from string import ascii_lowercase

# Handle command line arguments
input = sys.argv[1]
output = sys.argv[2]

# Setup
questions = {}
with open(input, "r") as f:
    lines = f.readlines()

# Read input file
reading_question = True
for line in lines:
    line = line.strip()

    # Skip blank lines
    if not line.strip():
        reading_question = True
        continue
    # Add new question value
    if reading_question:
        question = line.strip()
        questions[question] = []
        reading_question = False
    # Add new answer choice as value to question key
    else:
        questions[question].append(line.strip())

# Write output file
num_of_questions = len(questions)
with open(output, "w") as f:
    # Iterate through questions
    for i, question in enumerate(questions.keys()):
        f.write(str(i + 1) + ". (1 point)\n" + question + "\n")

        num_of_answers = len(questions[question])
        # Iterate through answer choices
        for j, answer in enumerate(questions[question]):
            if answer[0] == "*":
                f.write("*" + ascii_lowercase[j] + ". " + answer[1:] + "\n")
            else:
                f.write(ascii_lowercase[j] + ". " + answer + "\n")

        f.write("#randomize\n\n")

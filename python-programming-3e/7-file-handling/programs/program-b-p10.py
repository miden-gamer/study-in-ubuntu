# PROGRAM 7.10 : Write a program that generates a Quiz and uses two files - 
# questions.txt and answers.txt. The program opens questions.txt and reads a 
# question and displays the question with options on the screen. The program 
# then opens the answer.txt file and displays the correct answers.

import os

questions_file = os.path.join(os.path.dirname(__file__), "example-files", "r-b-p10-questions.txt")
answers_file = os.path.join(os.path.dirname(__file__), "example-files", "r-b-p10-answers.txt")

with open(questions_file, "r") as qf:
    ques = qf.read()

qlines = ques.split('\n')
for line in qlines:
    print(line)

with open(answers_file, "r") as af:
    ans = af.read()

print("\nCorrect Answers:")

alines = ans.split('\n')
for line in alines:
    print(line)
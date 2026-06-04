questions = {
    "What is the capital of France?": "paris",
    "What is 5 + 7?": "12",
    "Which language is used for Data Science?": "python"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.lower() == answer:
        score += 1

print(f"\nFinal Score: {score}/{len(questions)}")





What is the capital of France?  Paris
What is 5 + 7?  13
Which language is used for Data Science?  python

Final Score: 2/3
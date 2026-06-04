# Quiz Application in Python

## Overview

This program simulates a simple quiz application.

Users answer a set of questions and receive a final score based on correct answers.

The project demonstrates dictionaries, loops, conditional logic, scoring systems, and user interaction.

---

## Code

```python
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
```

---

## How It Works

1. Questions and answers are stored in a dictionary
2. The program loops through each question
3. The user submits an answer
4. Answers are compared with the correct solution
5. The score increases for each correct answer
6. The final score is displayed

---

## Example Run

### Input

```text
What is the capital of France? paris
What is 5 + 7? 12
Which language is used for Data Science? python
```

### Output

```text
Final Score: 3/3
```

---

## Concepts Covered

- Dictionaries
- Loops
- Conditional statements
- User input handling
- Scoring systems

---

## Why This Program?

This project introduces:

- Quiz and assessment systems
- User interaction workflows
- Score tracking
- Data validation

These concepts are commonly used in:

- Online examinations
- Learning platforms
- Certification systems
- Educational applications

---

## Possible Improvements

- Multiple-choice questions
- Timer functionality
- Difficulty levels
- Randomized questions
- Store high scores in a file

---

## Author

Daily Python Practice  
Quiz Application

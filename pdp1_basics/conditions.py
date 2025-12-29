'''
Conditions - Python Basics

Covered: 
- if/elif/else
- Comparision Operators


'''

## Voting Eligibility
mage = int(input('Enter your age: '))

if mage>18:
    print('You can vote! ')
else:
    print('Become 18 y first')



## Grading Eligibility
score = int(input("Enter your score: "))


if score>=90:
    print("Grade A")
elif score >=75:
    print("Grade B")
elif score >=60:
    print("Grade C")
else:
    print("Too Bad")



## Experience level
yoex = int(input("Enter your years of experience: "))


if yoex < 3:
    print('Entry level: ')
elif 3<yoex<7:
    print("Mid Level")
else:
    print("Senior Level")

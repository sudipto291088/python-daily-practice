
'''
Loops

- for loops
- while loops
- continue
- list comprehension


'''




for i in range(5):
    print(i)


for i in range(1,6):
    print(f"count: {i}")


languages = ["Python"," R","SQL","JS"]

for lang in languages:
    print(lang)


count = 1

while count <=5:
    print(count)
    count += 1


n = int(input('enter a number to print from 1: '))

for i in range(1,n+1):
    if i ==3:
        continue
    print(i)

a = int(input('Enter a number: '))

numbers = [i for i in range(1,a+1) if i!=3]
print(numbers)
text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)




Enter a string:  Sudipto is studying Artificial Intelligence
Uppercase letters: 3
Lowercase letters: 36
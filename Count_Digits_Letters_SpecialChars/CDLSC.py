text = input("Enter a string: ")

letters = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)




Enter a string:  Hello How are you doing 13
Letters: 19
Digits: 2
Special characters: 5




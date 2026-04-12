def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


s = input("Enter a string: ")

if is_palindrome(s):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")





Enter a string:  malayalam
The string is a palindrome
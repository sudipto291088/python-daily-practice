try:
    a = 10
    b = int(input('Enter a number: '))
    print(a/b)
except Exception as err:
    print(f"root cause of exception is: {err}")
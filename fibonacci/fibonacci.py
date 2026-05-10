n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a)
    a, b = b, a + b



Enter the number of terms:  9
Fibonacci Series:
0
1
1
2
3
5
8
13
21
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)




Enter start number:  9
Enter end number:  29
Prime numbers are:
11
13
17
19
23
29
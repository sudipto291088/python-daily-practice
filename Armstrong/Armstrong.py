num = int(input("Enter a number: "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp = temp // 10

if num == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")




Enter a number:  4567
Not an Armstrong Number
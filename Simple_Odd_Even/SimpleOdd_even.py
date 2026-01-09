odd = []
even = []

a = int(input('Enter a range for the array'))


for i in range(a):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print (odd,even)
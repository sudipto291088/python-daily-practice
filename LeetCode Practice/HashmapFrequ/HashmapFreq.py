a = int(input('Enter a range for the array'))
arr = []
count = {}
max_count = 0
most_frequent = None


for i in range(a):
    i = int(input())
    arr.append(i)



for num in arr:
    if num in count:
        count[num] = count[num]+1
    else:
        count[num] = 1

    if count[num]>max_count:
        max_count = count[num]
        most_frequent = num

print(f'the most frequent number is {most_frequent}')
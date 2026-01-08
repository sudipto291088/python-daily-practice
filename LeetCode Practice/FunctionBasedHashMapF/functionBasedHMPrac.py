def most_frequent(arr):
    count = {}
    max_count = 0
    frequent = None

    for i in arr:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i] = 1

        if count[i]>max_count:
            max_count = count[i]
            frequent = i

    return i


def user_input():
    a = int(input('Enter a range for your array: '))
    marr = []
    for m in range(a):
        m = int(input())
        marr.append(m)

    return marr


if __name__ == "__main__":
    marr = user_input()
    result = most_frequent(marr)
    print(f"The most frequent number is {result}")
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


s = input("Enter a sentence: ")

result = word_frequency(s)

for word, count in result.items():
    print(f"{word} : {count}")





Enter a sentence:  Python is powerful
python : 1
is : 1
powerful : 1
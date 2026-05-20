sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))



Enter a sentence:  i am loving my time on earth
Longest word: loving
Length: 6

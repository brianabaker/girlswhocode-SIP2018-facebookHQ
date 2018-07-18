
sentence = "i love CHEESE and cheese loves me and clouds are love"

word_count = {}

for word in sentence.split():
    if word.lower() not in word_count:
        word_count[word.lower()] = 1
    else:
        word_count[word.lower()] += 1

print(word_count)

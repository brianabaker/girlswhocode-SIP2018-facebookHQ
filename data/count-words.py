import re
sentence = "I love the smell of roses they smell like roses and angels with wings and roses"

list_of_words = sentence.split()
print(list_of_words)
word_count = {}

for word in list_of_words:
    if word not in word_count:
        word_count[word.lower()] = 0
    word_count[word.lower()] += 1

print(word_count)

# s = "I am. With? So May!"
# s = re.sub(r'[^\w\s]','',s)

f = open("fake-dictionary.txt","r")

blah = []
for line in f:
    print(line.strip())
    blah.append(line.strip())
print(blah)

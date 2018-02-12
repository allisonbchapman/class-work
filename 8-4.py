try:
    fhand = open(input('Enter file: '))
except:
    print('Error')
    exit()
vocabulary = []
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)
vocabulary.sort()
print(vocabulary)
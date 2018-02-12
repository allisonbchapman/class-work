fhand = open('words.txt')
dictionary = dict()
for line in fhand:
    words = line.split()
    for word in words:
        dictionary[word] = 'val'
search = input('Enter word: ')
if search in dictionary:
    print('The word ', search, 'does appear in this file')
else:
    print('The word ', search, 'does not appear in this file')
import string
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File could not be opened.')
    exit()
letters = dict()
for line in fhand:
    line = line.strip()
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.translate(line.maketrans('','', string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for ch in word:
            if ch not in letters:
                letters[ch] = 1
            else:
                letters[ch] +=1
lst = list()
for key, val in list(letters.items()):
    lst.append((val, key))
lst.sort(reverse = True)
for key, val in lst:
    print (key, val)
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File could not be opened.')
    exit()
fr = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) <3: continue
    if words[0] == 'From':
        fraddress = words[1]
        delimiter = fraddress.find('@') + 1
        domain = fraddress[delimiter: ]
        if domain not in fr:
            fr[domain] = 1
        else:
            fr[domain] += 1
print(fr)
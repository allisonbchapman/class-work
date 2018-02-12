fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File could not be opened.')
    exit()
dow = dict()
for line in fhand:
    words = line.split()
    if len(words) <3: continue
    if words[0] == 'From':
        day = words[2]
        if day not in dow:
            dow[day] = 1
        else:
            dow[day] += 1
print(dow)
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File could not be opened.')
    exit()
fr = dict()
for line in fhand:
    words = line.split()
    if len(words) <3: continue
    if words[0] == 'From':
        fraddress = words[1]
        if fraddress not in fr:
            fr[fraddress] = 1
        else:
            fr[fraddress] += 1
lst = list()
for key, value in list(fr.items()):
    lst.append((value,key))
lst.sort(reverse = True)
for key, value in lst[:1]:
    print(value, key)
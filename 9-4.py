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
for key in fr:
    if fr[key] == max(fr.values()):
        print(key, fr[key])
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File could not be opened.')
    exit()
hours = dict()
for line in fhand:
    words = line.split()
    if len(words) <6: continue
    if words[0] == 'From':
        time = words[5]
        hour, minute, second = time.split(':')
        if hour not in hours:
            hours[hour] = 1
        else:
            hours[hour] += 1
lst = list()
for key, value in list(hours.items()):
    lst.append((key, value))
lst.sort()
for key, value in lst:
    print(key, value)
    
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
confidence = 0
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        line = line[19:]
        count = count + 1
        confidence = confidence + float(line)
print('Average spam confidence: ', confidence/count)
fname = input('enter file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
rd = open(fname)

for line in rd:
    line = line.strip()
    line = line.split(":")[:3]
    print(line)
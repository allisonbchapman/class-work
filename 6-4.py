str = 'X-DSPAM-Confidence:0.8475'
colonpos = str.find(':')
number = str[colonpos+1:]
print(float(number))
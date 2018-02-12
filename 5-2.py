total = 0
count = 0
maximum = None
minimum = None
while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        total = total + float(number)
        count = count + 1
        if maximum == None or number > maximum:
            maximum = number
        if minimum == None or number < minimum:
            minimum = number
    except:
        print('Invalid input')
print(total, count, maximum, minimum)

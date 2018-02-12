total = 0
count = 0
while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        total = total + float(number)
        count = count + 1
    except:
        print('Invalid input')
print(total, count, total/count)
numbers = []
while True:
    try:
        inp = input('Enter a number: ')
        if inp == 'done':
            break
        number = float(inp)
        numbers.append(number)
    except:
        print('Invalid input')
print('Maximum: ', max(numbers))
print('Minimum: ', min(numbers))
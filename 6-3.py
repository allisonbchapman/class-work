def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    return count
string = input('Please enter a string: ')
letter = input('What letter are you looking for? ')
print('The letter ' + str(letter) + ' appears ' + str(count(string, letter)) + ' time(s) in ' + str(string))
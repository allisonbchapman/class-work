index = -1
word = input("Please enter a word: ")
while index >= -(len(word)):
    letter = word[index]
    print(letter)
    index = index - 1
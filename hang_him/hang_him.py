# player life
life = 1
# create the word to guess
word = list('test')
userWord = list(range(0, len(word)))
# create final word
result = ""

# create the word for display
for index in range(0, len(word)):
    if isinstance(userWord[index], int):
        result += "_ "
    else:
        result += f'{userWord[index]}'

print(f'word to guess: {result}')

# player is playing while he have life
while life > 0:
    result = ""
    # user enter letter
    userLetter = input('enter letter: ')

    # check if letter exist in the word
    for index in range(0, len(word)):
        if userLetter == word[index]:
            userWord[index] = userLetter

    # create the word for display properly
    for index in range(0, len(word)):
        if isinstance(userWord[index], int):
            result += "_ "
        else:
            result += f'{userWord[index]} '

    print(f'word to guess: {result}')

    # check if the world is complete
    if userWord == word:
        life = 0
    life -= 1

if userWord != word:
    print('=====================\nyou lose !\n=====================')
else:
    print('=====================\nyou win !\n=====================')

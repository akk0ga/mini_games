# player life
life = 10
# create the word to guess
word = list('test')
userWord = list(range(0, len(word)))
active = True


def word_display():
    result = ""
    for letter in range(0, len(word)):
        if isinstance(userWord[letter], int):
            result += "_ "
        else:
            result += f'{userWord[letter]} '
    return result


# display word
print(f'word to guess: {word_display()}')
# player is playing while he have life
while life > 0 and active:
    # user enter letter
    userLetter = input('enter letter: ')

    # check if letter exist in the word
    for index in range(0, len(word)):
        if userLetter == word[index]:
            userWord[index] = userLetter
        elif index == len(word) - 1 and userLetter not in word:
            life -= 1
            print(f'letter incorrect you have now {life} life')

    # create the word to display it properly
    print(f'word to guess: {word_display()}')

    # check if the world is complete
    if userWord == word:
        active = False

if userWord != word:
    print('=====================\nyou lose !\n=====================')
else:
    print(f'=====================\nyou win with {life} life !\n=====================')

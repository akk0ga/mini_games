from random_words import RandomWords

def generation_word():
    random_words = RandomWords()
    word = random_words.random_word()
    return word


def word_display():
    result = ""
    for letter in range(0, len(word)):
        if isinstance(userWord[letter], int):
            result += "_ "
        else:
            result += f'{userWord[letter]} '
    return result


# player life
life = 10
# create the word to guess
complete_word = generation_word()
word = list(complete_word)
userWord = list(range(0, len(complete_word)))
active = True

# display total letter
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
    print(f'=====================\nyou lose ! the word was {complete_word}\n=====================')
else:
    print(f'=====================\nyou win with {life} life !\n=====================')

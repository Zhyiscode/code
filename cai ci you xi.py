import random

live: int = 3
# words = ['pizza', 'fairy', 'teech', 'shit', 'otter', 'plane']
words = ['aba','abc','abb','abd']
secret_word = random.choice(words)

clue = list('?????')
heart_symbol = u'\u2764'

guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter[index] != secret_word[index]:
            clue[index] = guessed_letter[index]
        else:
            index = index + 1


while live > 0:
    print(clue)
    print('剩余生命次数' + heart_symbol * live)
    guess = input("猜测字母或者整个单词：")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    # if guess in secret_word:
    #     update_clue(guess, secret_word, clue)
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
        if "?" not in secret_word:
            guessed_word_correctly = True
            break

    else:
        print("错误，你丢了一条命\n")
        live = live - 1
if guessed_word_correctly:
    print("你赢了秘密单词是：" + secret_word)
else:
    print("你输了，秘密单词是：" + secret_word)

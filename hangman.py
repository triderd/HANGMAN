import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
 'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
 'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
 'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}



def print_word(guessed, secret_word):
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in guessed:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def guess_letter(already_guessed):
    while True:
        letter = input('введи букву тока не нада ввадить эти буквы:' + already_guessed + '\n')
        if len(letter) != 1:
            print('бро сори канечна но нескалька букф ввадить нельзя')
        elif letter in already_guessed:
            print('я канешна извеняюсь но ты ету букву уже писал так что перепеши сваю букву')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print(
                'я очинь деликатная машина я русские буквы не принимаю и знаки тоже тока англиские бквы так что перепиши пж')
        else:
            return letter


def display_board(guessed, missed, secret_word):
    tries = len(missed)
    print(HANGMANPICS[tries])
    print('Missed letters:', end=' ')
    for letter in missed:
        print(letter)
    print_word(guessed, secret_word)


def random_topic_and_word(words):
    topic = random.choice(list(words.keys()))
    words_by_key = words[topic]
    word_index = random.randint(0, len(words_by_key) - 1)
    return topic,words_by_key[word_index]


def found_all(guessed, secret_word):
    for i in range(len(secret_word)):
        if secret_word[i] not in guessed:
            return False
    return True


def play_again():
    play_again = input('хочишь ли ты сыграть снова?')
    return play_again.lower().startswith('y')


def init_state():
    guessed = ''
    missed = ''
    game_done = False
    topic,secret_word = random_topic_and_word(WORDS)
    return guessed,missed,game_done,topic,secret_word

guessed,missed,game_done,topic,secret_word = init_state()

while True:
    print("Тема НАШЕЙ ИГРЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ: "+topic)
    display_board(guessed, missed, secret_word)
    already_guessed = guessed + missed
    letter = guess_letter(already_guessed)
    if letter in secret_word:
        guessed += letter
    else:
        missed += letter
    if found_all(guessed, secret_word):
        print('бро ты выйграл')
        game_done = True
    elif len(missed) == len(HANGMANPICS) - 1:
        display_board(guessed, missed, secret_word)
        print('бро сори ты праиграл')
        print('это слово было:' + secret_word)
        game_done = True
    if game_done:
        if play_again():
            guessed,missed,game_done,topic,secret_word = init_state()
        else:
            break



import random
from string import ascii_lowercase

words = 'python', 'java', 'kotlin', 'javascript'
running = True

while running:
    print("H A N G M A N")
    game_word = random.choice(words)
    shadow_word = "-" * len(game_word)
    lives = 8
    chars_set = set()
    user_input = input('Type "play" to play the game, "exit" to quit: ')

    if user_input == "play":
        while lives:
            print(f"\n{shadow_word}")
            char = input("Input a letter: ")
            if len(char) != 1:
                print("You should input a single letter")
                continue
            elif char not in ascii_lowercase:
                print("Please enter a lowercase English letter")
                continue
            elif char in game_word and char not in shadow_word:
                dictionary = {pos: value for pos, value in enumerate(game_word) if value == char}
                for pos, value in dictionary.items():
                    shadow_word = ''.join((shadow_word[:pos], value, shadow_word[pos + 1:]))
            else:
                if char in chars_set:
                    print("You've already guessed this letter")
                    continue
                else:
                    print("That letter doesn't appear in the word")
                lives -= 1
            chars_set.add(char)

            if "-" not in shadow_word:
                print("You guessed the word!\nYou survived!\n")
                break
            if lives == 0:
                print("You lost!\n")
    else:
        running = False

import random

words = 'python', 'java', 'kotlin', 'javascript'
game_word = random.choice(words)
attempts = 8
shadow_word = "-" * len(game_word)

print("H A N G M A N")
while attempts != 0:
    print(f"\n{shadow_word}")
    char = input("Input a letter: ")
    if char in game_word:
        dictionary = {pos: value for pos, value in enumerate(game_word) if value == char}
        if char not in shadow_word:
            for pos, value in dictionary.items():
                shadow_word = ''.join((shadow_word[:pos], value, shadow_word[pos + 1:]))
        else:
            print("No improvements")
            attempts -= 1
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
    if "-" not in shadow_word:
        print("You guessed the word!\nYou survived!")
        break
    if attempts == 0:
        print("You lost!")


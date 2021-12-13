import random

print("H A N G M A N")
words = 'python', 'java', 'kotlin', 'javascript'
game_word = random.choice(words)
if input("Guess the word: ") == game_word:
    print("You survived!")
else:
    print("You lost!")

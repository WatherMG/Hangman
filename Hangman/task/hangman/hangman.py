import random

print("H A N G M A N")
words = 'python', 'java', 'kotlin', 'javascript'
game_word = random.choice(words)
if input(f"Guess the word {game_word[:3]}{'-' * (len(game_word) -3 )}: ") == game_word:
    print("You survived!")
else:
    print("You lost!")

import random

words = ["python", "computer", "program", "keyboard", "internet"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman Game")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)

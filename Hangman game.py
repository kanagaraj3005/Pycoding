import random

words = ['python', 'programming', 'hangman', 'challenge']
secret_word = random.choice(words)
display = ["_" for _ in secret_word]
turns = 7
guessed_letters = []

print("Welcome to Hangman!")

while turns > 0 and "_" in display:
    print("\n" + " ".join(display))
    print(f"Turns left: {turns}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i, char in enumerate(secret_word):
            if char == guess:
                display[i] = guess
        print("Correct guess!")
    else:
        turns -= 1
        print("Wrong guess!")

if "_" not in display:
    print("\n" + " ".join(display))
    print("Congratulations! You guessed the word. You Win!")
else:
    print("\n" + " ".join(display))
    print(f"You ran out of turns. The word was: {secret_word}. You Lose!")

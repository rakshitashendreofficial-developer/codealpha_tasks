import random

# Step 1: Create a list of words
words = ["python", "apple", "chair", "house", "river"]

# Step 2: Randomly choose a word
secret_word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

# Step 4: Game loop
while incorrect_guesses < max_guesses:

    display_word = ""

    # Step 5: Display guessed letters and underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_guesses - incorrect_guesses)

    # Step 6: Check if the player won
    if "_" not in display_word:
        print("🎉 You win! The word was:", secret_word)
        break

    # Step 7: Get user input
    guess = input("Guess a letter: ").lower()

    # Step 8: Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Step 9: Check if guess is wrong
    if guess not in secret_word:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

# Step 10: Loss condition
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over! The word was:", secret_word)

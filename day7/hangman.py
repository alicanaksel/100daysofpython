import random
import hangmanart

# --- Word banks (20 each) ---
easy_words = [
    "cat", "dog", "sun", "book", "tree",
    "fish", "star", "milk", "ball", "car",
    "house", "chair", "table", "pen", "cup",
    "hat", "rain", "shoe", "bird", "apple"
]

medium_words = [
    "planet", "castle", "garden", "rocket", "bridge",
    "silver", "monkey", "prison", "yellow", "market",
    "butter", "cloudy", "forest", "friend", "window",
    "school", "dragon", "cheese", "pirate", "orange"
]

hard_words = [
    "elephant", "computer", "mountain", "triangle", "whistle",
    "journey", "diamond", "volcano", "library", "zombie",
    "gravity", "pyramid", "network", "kingdom", "phantom",
    "oxygen", "justice", "quantum", "mystery", "crystal"
]

# --- Start ---
print(hangmanart.entrance)
print("Welcome to Hangman!")

# Choose difficulty
while True:
    level = input("Choose your level (1=Easy, 2=Medium, 3=Hard): ").strip()
    if level in {"1", "2", "3"}:
        break
    print("Invalid choice. Please type 1, 2, or 3.")

if level == "1":
    secret = random.choice(easy_words)
elif level == "2":
    secret = random.choice(medium_words)
else:
    secret = random.choice(hard_words)

# Initial setup
display = ["_"] * len(secret)
guessed = set()
stages = hangmanart.mistakes   # mistake0 .. mistake6
wrong_guesses = 0
lives = len(stages) - 1        # 6 lives (7 stages total)

print(" ".join(display))

# --- Main loop ---
while "_" in display and wrong_guesses < len(stages):
    guess = input("Guess a letter: ").strip().lower()

    # Check input validity
    if len(guess) != 1 or not guess.isalpha():
        print("Please guess a single alphabetic letter.")
        continue

    # Already guessed?
    if guess in guessed:
        print("You've already guessed that letter.")
        continue
    guessed.add(guess)

    # If correct guess
    if guess in secret:
        for i, ch in enumerate(secret):
            if ch == guess:
                display[i] = guess
        print("Good guess!")
        print(" ".join(display))
    else:
        # Print current stage before incrementing
        print("That letter is not in the word.")
        print(stages[wrong_guesses])   # first wrong prints mistake0
        wrong_guesses += 1
        lives -= 1
        print(f"Lives left: {lives}")
        print(" ".join(display))

    # Win condition
    if "_" not in display:
        print("\nYou win! 🎉")
        print(f"The word was: {secret}")
        break

# Lose condition
if wrong_guesses >= len(stages):
    print("\nGAME OVER!")
    print(f"The word was: {secret}")

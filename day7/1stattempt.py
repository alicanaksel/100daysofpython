import hangmanart, random
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

print(f"{hangmanart.entrance}\nWelcome to the hangman!")

level=int(input("Choose your level. Type 1, 2 or 3\n1)Easy\n2)Medium\n3)Hard\n"))
word=[]
if level==1:
    for i in random.choice(easy_words):
        word.append(i)
elif level==2:
    for i in random.choice(medium_words):
        word.append(i)
elif level==3:
    for i in random.choice(hard_words):
        word.append(i)
else:
    print("Wrong input.")
    exit()

print("_ "*len(word))
guessed= set()
life=6

def art_printer(number: int):
    print(hangmanart.mistakes[number])

while not len(word)==0:
    guess=input("Guess a letter!\n")
    if len(guess)==1:
        for i in range(0,life):
            if guess not in word:
                if life >0:
                    life -= 1
                    art_printer(i)
                    print("It's not in the word")
                    guess=input("Guess a letter!\n")
                else:
                    art_printer(6)
                    print("\nGAME OVER!!!!!")
                    exit()
            else:


        if guess not in guessed:
            guessed.add(guess)
        else:
            print("You already typed this letter!")
    else:
        print("You can guess only one letter at a time")
        guess=input("Guess a letter!\n")

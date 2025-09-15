import random
welcome=r"""
 _                 _______  ______   _______  _______    _______           _______  _______  _______  _______  _______ 
( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )  (  ____ \|\     /|(  ____ \(  ____ \(  ____ \(  ____ \(  ____ )
|  \  ( || )   ( || () () || (   ) )| (    \/| (    )|  | (    \/| )   ( || (    \/| (    \/| (    \/| (    \/| (    )|
|   \ | || |   | || || || || (__/ / | (__    | (____)|  | |      | |   | || (__    | (_____ | (_____ | (__    | (____)|
| (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)  | | ____ | |   | ||  __)   (_____  )(_____  )|  __)   |     __)
| | \   || |   | || |   | || (  \ \ | (      | (\ (     | | \_  )| |   | || (            ) |      ) || (      | (\ (   
| )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__  | (___) || (___) || (____/\/\____) |/\____) || (____/\| ) \ \__
|/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/  (_______)(_______)(_______/\_______)\_______)(_______/|/   \__/
                                                                                                                       

                                                                                                                       
"""
print(welcome)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
number= random.randint(1,100)
difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty== "easy":
    attempts=10
    print(f"You have {attempts} attempts ramaining to guess the number.")
elif difficulty =="hard":
    attempts=5
    print(f"You have {attempts} attempts ramaining to guess the number.")
else:    
    print("Invalid typing. Quiting...")
    exit()


while attempts !=0:
    
    guess=int(input("Make a guess: "))

    if guess != number:
        if guess > number:
            print("Too high.\n Guess again.")
            attempts -=1
            print(f"You have {attempts} attempts ramaining to guess the number.")
        elif guess < number:
            print("Too low.\n Guess again.")
            attempts -=1
            print(f"You have {attempts} attempts ramaining to guess the number.")
    else:
        print(f"You got it! The answer was {number}.")
        break

if attempts == 0:
    print("You lose.")

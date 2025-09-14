print("Welcome to the secret auction program.")
bidders=dict()
while True:
    name= input("What's your name?: ").lower()
    bid=int(input("What's your bid?: $"))
    bidders.update({name:bid })
    ask= input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if ask== "yes":
        continue
    elif ask=="no":
        break
    else:
        print("Invalid input. Quitting the program.")
        break


max_score=0
for i in bidders.values():
    if i > max_score:
        max_score=i

'''
Thanks to stackoverflow
Basically, it separates the dictionary's values in a list, finds the position of the value you have, and gets the key at that position.

More about keys() and .values() in Python 3
'''
name= list(bidders.keys())[list(bidders.values()).index(max_score)]
print(f"The winner is {name} with a bid of ${max_score} ")
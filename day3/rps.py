import random
rock= r'''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\

'''
scissors= r'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''

paper=r'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|         
'''

choose= int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors\n"))
comp_num= random.randint(0,2)

if choose== 0:
    print(rock)
    if comp_num== 0:
        print(f"Computer chose:\n{rock}")
        print("Draw")
    elif comp_num== 1:
        print(f"Computer chose:\n{paper}")
        print("You lose")
    else:
        print(f"Computer chose:\n{scissors}")
        print("You win")
elif choose== 1:
    print(paper)
    if comp_num== 0:
        print(f"Computer chose:\n{rock}")
        print("You win")
    elif comp_num== 1:
        print(f"Computer chose:\n{paper}")
        print("Draw")
    else:
        print(f"Computer chose:\n{scissors}")
        print("You lose")
elif choose == 2:
    print(scissors)
    if comp_num== 0:
        print(f"Computer chose:\n{rock}")
        print("You lose")
    elif comp_num== 1:
        print(f"Computer chose:\n{paper}")
        print("You win")
    else:
        print(f"Computer chose:\n{scissors}")
        print("Draw")
else:
    print("invalid input")
import random
import time

opt = ['snake', 'water', 'gun']

def user_won(pc_choice, usr_choice):
    if pc_choice=='snake' and usr_choice=='gun':
        return True
    if pc_choice=='water' and usr_choice=='snake':
        return True
    if pc_choice=='gun' and usr_choice=='water':
        return True
    return False

def pc_won(pc_choice, usr_choice):
    if usr_choice=='snake' and pc_choice=='gun':
        return True
    if usr_choice=='water' and pc_choice=='snake':
        return True
    if usr_choice=='gun' and pc_choice=='water':
        return True
    return False


def playGame():
    pc_score = 0
    usr_score = 0
    games = 1
    while games <= 5: 
        usr_choice = input("Select one (snake/water/gun): ")
        pc_choice = random.choice(opt)
        print(f"Our choice: {pc_choice}")
        time.sleep(1)
        if user_won(pc_choice, usr_choice):
            usr_score += 1
            print("Yss")
        elif pc_won(pc_choice, usr_choice):
            pc_score += 1 
            print("Noo")
        else:
            print("Close")
        games += 1
        time.sleep(2)

    if (pc_score < usr_score):
        print("Hurray! You won\n")
    elif (pc_score > usr_score):
        print("Psst, you lost\n")
    else:
        print("That was close\n")


print("*****Welcome to Snake Water Gun game*****\n\n")
res = input("Play a game? (y/n): ")
if res==False:
    exit()
playGame()
while(1):
    res = input("Wanna play again? (y/n): ")
    if res=='n':
        exit()
    playGame()
    

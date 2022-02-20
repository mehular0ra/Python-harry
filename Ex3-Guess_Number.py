import random

print("*****Guess Number Game*****\n\n")

def game():
    real_num = random.randint(1, 10)
    num = int(input("Guess a number between 1 to 10 (you have five chances): "))
    total_chances = 5
    count = 1
    won = False
    while count <= total_chances:
        if num == real_num:
            won = True
            break
        elif num < real_num:
            print("The number is greater than you guessed")
        else:
            print("The number is smaller than you guessed")
        num = int(input("Guess again: "))
        count += 1
    if won == True:
        print("Congrats! You got it right.")
    else:
        print("You ran out of number of changes. Better lunch Nex time :>")


play_again = True
while play_again == True:
    game()
    ask = input("Do you want to play again? (y/n): ")
    if ask == 'n':
        play_again = False
print("See you again...")

    


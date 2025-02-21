import random

def roll_dice():
      return random.randint(1,6)

def play_game():
        print("Welcome your dice awaits you")    
        print("Enter to roll the dice")
        input()
        player_dice=roll_dice()
        computer_dice=roll_dice()
        print("You rolled ",player_dice)
        print("Computer rolled ",computer_dice)
        if player_dice>computer_dice:
            print("YOU WIN!")
        elif player_dice==computer_dice:
            print("ITS A TIE")
        else:
            print("BETTER LUCK NEXT TIME")        
while True:
    play_game()
    print("Do you want to play again?///(YES OR NO)")    
    choice=input("Enter Your choice::")
    if choice.strip().lower()== "no" :
        print("THANKS FOR PLAYING")
        break       
    
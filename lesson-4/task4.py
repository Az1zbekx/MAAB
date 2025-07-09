import random
def game():

    num = random.randint(1,100)
    c  = 10

    while c:
        x = input()

        if not x.isdigit():
            print("Please enter a valid number.")
            continue
        
        x = int(x) 
        
        if x == num:
            print("You guessed it right!")
            return
        elif x > num:
            print("Too high!")
        elif x < num:
            print("Too low!")

        c -= 1

    print("You lost. Want to play again?")
    com = input().strip().lower()
    if com in ['y', 'yes', 'ok']:
        game()
    
game()
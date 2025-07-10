import random
def game():

    num = random.randint(1,100)
    cnt  = 10

    while c:
        guess = input()

        if not guess .isdigit():
            print("Please enter a valid number.")
            continue
        
        guess  = int(guess ) 
        
        if guess  == num:
            print("You guessed it right!")
            return
        elif guess  > num:
            print("Too high!")
        elif guess  < num:
            print("Too low!")

        cnt -= 1

    print("You lost. Want to play again?")
    com = input().strip().lower()
    if com in ['y', 'yes', 'ok']:
        game()
    
game()
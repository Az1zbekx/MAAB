import random

options = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while user_score < 5 and computer_score < 5:
    user = input("Choose rock, paper, or scissors: ").lower().strip()
    if user not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")
    print("-" * 30)

if user_score == 5:
    print("🎉 You won the match!")
else:
    print("💻 Computer won the match!")

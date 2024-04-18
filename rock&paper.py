import random

player = ["rock", "paper", "scissors"]
computer = random.choice(player)

player = input("Enter a choice (rock, paper, scissors): ")

print(f"player:{player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You lose!")
print("play again")

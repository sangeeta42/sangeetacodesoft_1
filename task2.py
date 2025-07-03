import random

# Choices
choices = ["rock", "paper", "scissors"]

# Score
user_score = 0
computer_score = 0

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    global user_score, computer_score
    print("\n--- Rock-Paper-Scissors ---")
    print("Choose: Rock, Paper, or Scissors")

    user_choice = input("Your choice: ").strip().lower()
    while user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Your choice: ").strip().lower()

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice.capitalize()}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        play_round()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 You are the overall winner!")
            elif user_score < computer_score:
                print("💻 Computer is the overall winner!")
            else:
                print("It's a final tie!")
            break

if __name__ == "__main__":
    main()
# this app is about rock, paper, scissors game
def main():
    print("Hello, welcome to the rock, paper, scissors game!")

    user_points = 0
    computer_points = 0

    while True:
        print("Please enter your choice: rock, paper, or scissors")
        user_choice =  input().lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please try again.")
            continue

        import random
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(f"Computer choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            user_points += 1
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            user_points += 1
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            user_points += 1
            print("You win!")
        else:
            computer_points += 1
            print("You lose!")

        print("Do you want to play again? (yes/no)")
        play_again = input()
        if play_again != "yes":
            print(f"User points: {user_points}, Computer points: {computer_points}")
            break

if __name__ == "__main__":
    main()
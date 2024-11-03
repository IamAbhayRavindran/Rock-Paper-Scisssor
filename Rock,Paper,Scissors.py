import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    return 'lose'

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    
    while True:
        player_choice = input("Enter 'rock' for Rock, 'paper' for Paper, or 'scissors' for Scissors: ").strip().lower()
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        if result == 'win':
            print("You win!")
        elif result == 'tie':
            print("It's a tie!")
        else:
            print("You lose!")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
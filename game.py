import random

# Get player's name
player = input("Enter your name: ")
print(f"Greetings, {player}! Welcome to the Game of Luck!")

# Display game rules
rules = (
    "Rules:\n"
    "- Rock vs Scissors:\t Rock wins\n"
    "- Rock vs Paper:\t Paper wins\n"
    "- Paper vs Scissors:\t Scissors wins\n"
)
print(rules)

# Start game loop
while True:
    # Ask for permission to continue
    permission = input("Are you ready to play? Y/N: ").upper()
    if permission == "N":
        print(f"Thank you for your time, {player}. Goodbye!")
        break
    elif permission == "Y":
        print("Let's start our game...")
        options = ["R", "P", "S"]
        choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        
        # Get player's choice with validation
        while True:
            a = input("Choose your option: R for Rock, P for Paper, S for Scissors: ").upper()
            if a in options:
                break
            else:
                print("Invalid choice. Please select R, P, or S.")
        
        # Computer's choice
        b = random.choice(options)
        print(f"{player} chose {choices[a]}")
        print(f"Computer chose {choices[b]}")
        
        # Determine the winner
        if a == b:
            print("Game is a tie: Both chose the same option.")
        elif (a == "R" and b == "S") or (a == "P" and b == "R") or (a == "S" and b == "P"):
            print(f"Congratulations {player}, you won the match!")
        else:
            print(f"You lose, {player}. Better luck next time!")
        print("\n")  # Add space before next round
    else:
        print("Invalid input. Please enter Y or N.")

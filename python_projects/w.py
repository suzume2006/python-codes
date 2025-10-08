import random

def roll_dice():
    # Generate a random number between 1 and 6
    dice = random.randint(1, 6)
    print(f"\n You rolled a {dice}!")

while True:
    input("Press Enter to roll the dice...")
    roll_dice()

    # Ask the user if they want to roll again
    play_again = input("Roll again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break

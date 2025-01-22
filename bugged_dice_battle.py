# Import the random module to easily generate pseudo-random numbers
import random

# Define a function that simulates a dice battle between two players
def dice_battle():

    # Generate random numbers between 1 and 6 for each player's die roll
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    # Compare the die rolls and return the result as a string
    if die_1 > die_2:
        return "Player 1 rolled a " + die_1 + " and Player 2 rolled a " + die_2 + ". Player 1 wins!"
    elif die_1 < die_2:
        return "Player 1 rolled a " + die_1 + " and Player 2 rolled a " + die_2 + ". Player 2 wins!"
    else:
        return "Player 1 rolled a " + die_1 + " and Player 2 rolled a " + die_2 + ". It's a tie!"

print(dice_battle())

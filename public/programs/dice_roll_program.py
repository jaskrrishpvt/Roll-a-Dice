from nada_dsl import *

def nada_main():
    player = Party(name="Player")

    # Dice roll: random number between 1 and 6
    dice_roll = (SecretInteger.random() % Integer(6)) + Integer(1)

    # Player's guess: number between 1 and 6
    player_guess = SecretInteger(Input(name="player_guess", party=player))

    # Compare the guess with the dice roll
    # 0 if not equal, 1 if equal
    result = (dice_roll == player_guess).if_else(Integer(1), Integer(0))

    # Outputs:
    # 1. The result (1 if player guessed correctly, 0 otherwise)
    # 2. The actual dice roll (so the player can verify)
    out_result = Output(result, "guess_result", player)
    out_dice_roll = Output(dice_roll, "actual_dice_roll", player)

    return [out_result, out_dice_roll]
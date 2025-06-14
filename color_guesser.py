import random

COLORS = ["R", "G", "B", "Y", "O", "P"]
TRIES = 10
CODE_LENGTH = 4

# Generate a color code
def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

# Guess color code
def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must enter a code of length {CODE_LENGTH}!")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color: {color}. Try again!")
                break
        else:
            break

    return guess


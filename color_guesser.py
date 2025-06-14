import random

COLORS = ["R", "G", "B", "Y"]
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

# Check color code
def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    #['G', 'Y', 'B', 'O']

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome come to color guesser! You have {TRIES} tries to guess the code...")
    print("Valid colors to guess: ", *COLORS)

    code = generate_code()
    
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You successfully guessed the code in {attempts} tries!")
            break

        print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")

    else:
        print("You ran out of tries. The code was: ", *code)

if __name__ == '__main__':
    game()
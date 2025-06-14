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
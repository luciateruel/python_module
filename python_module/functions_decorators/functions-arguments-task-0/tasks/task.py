from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    squares = {}
    for n in range(1, num +1):
        squares[n] = n*n
    return squares


generate_squares(5)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


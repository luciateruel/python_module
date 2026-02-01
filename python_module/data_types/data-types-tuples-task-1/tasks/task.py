from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    num = str(num)
    print(tuple(int(d) for d in num))
    return tuple(int(d) for d in num)


get_tuple(87178291199)



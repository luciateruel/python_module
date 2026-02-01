from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    final = []

    valid_indexes = sorted(i for i in indexes if 0 <= i <= len(s))

    start = 0
    for i in valid_indexes:
        final.append(s[start:i])
        start = i
    final.append(s[start:])

    return final




# split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# ```python
split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
split_by_index("no luck", [42])
# ["no luck"]
# ```

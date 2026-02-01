from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:

    if len(lst) < 2:

        return []

    new_l = []
    for n in range(len(lst) - 1):
        first_item = lst[n]
        second_item = lst[n+1]
        new_l.append((first_item, second_item))

    print(new_l)
    return new_l




get_pairs([1, 2, 3, 8, 9])
get_pairs(['need', 'to', 'sleep', 'more'])
get_pairs([1])


from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    s = s.lower()
    s_l = list(s)
    f_dic = {}

    for item in s:
        if item not in f_dic:
            f_dic[item] = 1

        else:
            f_dic[item] += 1
    print(f_dic)
    return f_dic



s = "Oh, it is python"

get_dict(s)



# Output: `{" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}`

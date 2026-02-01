from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    combined = {}

    for diccionario in args:
        for key, value in diccionario.items():
            if key not in combined:
                combined[key] = value
            else:
                combined[key] += value
    return  combined







dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
# >>> {'a': 300, 'b': 200, 'c': 300}
#
print(combine_dicts(dict_1, dict_2, dict_3))
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}


from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    l = []
    for num in range(1, n +1):
        if num % 5 == 0 and num % 3 == 0:
            value = 'FizzBuzz'
            l.append(value)
        elif num % 5 == 0:
            value = 'Buzz'
            l.append(value)
        elif num % 3 == 0:
            value = 'Fizz'
            l.append(value)
        else:
            l.append(num)

    print(l)
    return l




n = 10

get_fizzbuzz_list(n)
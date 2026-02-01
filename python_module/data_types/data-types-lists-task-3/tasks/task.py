from typing import List


def foo(nums: List[int]) -> List[int]:
    l = []
    for i in range(len(nums)):
        new_number = 1

        for n in range(len(nums)):
            if i == n:
                pass
            else:

                new_number *= nums[n]
        l.append(new_number)
    return l




nums = [1, 2, 3, 4, 5]

foo(nums)

if __name__ == "__main__":
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert foo([3, 2, 1]) == [2, 3, 6]
    assert foo([10]) == [1]
    assert foo([1, 0, 3]) == [0, 3, 0]
    assert foo([]) == []

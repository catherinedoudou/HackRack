def solution(num: int) -> int:
    binary_repr = bin(num)[2:]

    ones_index = [i for i, v in enumerate(binary_repr) if v == "1"]

    # ones_index = []
    # for idx, val in enumerate(binary_repr):
    #     if val == "1":
    #         ones_index.append(idx)

    if len(ones_index) <= 1:
        return 0
    else:
        gap = [j - i for i, j in zip(ones_index[:-1], ones_index[1:])]
        longest = max(gap)
        return longest - 1


# Brief
# find the binary represetation of a number
# calculate the longest sequence of zeros between two ones i.e.
# input (529) ----->>>> 1000010001
# output (4)


tests = {
    0: 0,
    1: 0,
    529: 4,
    9: 2,
    20: 1,
    15: 0,
    32: 0,
}

for test, result in tests.items():
    if solution(test) == result:
        print("OK:", test, result)
    else:
        print("Not working:", solution(test), result)


def solution2(num: int) -> int:
    if num == 0:
        return 0

    binary_repr = bin(num)[2:]
    res = 0
    for idx, val in enumerate(binary_repr.split("1")[:-1]):
        if idx == 0 and "0" in val:
            continue
        res = max(res, len(val))
    return res


def solution3(num: int) -> int:
    return max([0] + [len(i) for i in bin(num)[2:].split("1")[:-1]])

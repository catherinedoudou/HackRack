def median(arr):
    size = len(arr)
    if size % 2 == 0:
        mid = size // 2
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        mid = (size - 1) // 2
        return arr[mid]


def quartiles(arr):
    arr = sorted(arr)
    size = len(arr)
    Q1 = median(arr[: size // 2])
    Q2 = median(arr)
    if size % 2 == 0:
        Q3 = median(arr[size // 2 :])
    else:
        Q3 = median(arr[size // 2 + 1 :])
    return (Q1, Q2, Q3)


if __name__ == "__main__":
    median_tests = [
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]

    quartiles_tests = {
        (1, 2, 3, 4): [1.5, 2.5, 3.5],
        (1, 2, 3, 4, 5, 6, 7): [2, 4, 6],
    }

    # for test in median_tests:
    #     result = median(test)

    #     print(round(result, 1))

    for test, ans in quartiles_tests.items():
        print("-------------------")
        result = quartiles(test)

        print(result, ans)

        ## Option 1
        # for res in result:
        #     print(res)

        ## Option 2
        # [print(str(res)) for res in result]

        ## Option 3
        # print(*result, sep='\n', end='')

        ##Option 4
        # print(", ".join([str(res) for res in result]))

        ## Option 5
        # print(", ".join(map(str, result)))
def interQuartile(values, freqs):
    new_list = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            new_list.append(values[i])
    Q1, Q2, Q3 = quartiles(new_list)
    return Q3 - Q1

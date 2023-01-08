def br(n):
    binary_reper = bin(n)[2:]
    ones = binary_reper.split("0")
    length = []
    for one in ones:
        length.append(len(one))
    print(max(length))


br(13)

def collatz_conjecture(n):
    # seq = []
    while n > 1:
        # seq.append(n)
        if n % 2:
            n = (3 * n) + 1
        else:
            n = n // 2
    # seq.append(1)
    # print(seq)
    return n

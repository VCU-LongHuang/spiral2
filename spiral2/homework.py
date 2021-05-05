def spiralize(size, n=1):
    x = n
    counter = 0
    incrt = 2
    total = 0

    while x <= size ** 2:
        total += x
        x += incrt
        counter += 1
        if total == 4:
            incrt += 2
            counter = 0

    return total

    print(spiralize(501, 15))

def spiralize(size, n=1):

    x = n
    counter = 0
    incrt = 2
    Current_num = n
    total = 0

    while Current_num <= pow(size, 2) - 1:
        Current_num += incrt
        x += Current_num
        total += 1
        if total == 4:
            incrt += 2
            total = 0

    return x

    print(spiralize(501, 15))

def spiralize(number):
    return_value = 1
    diagonal = (number - 1) // 2
    return_value = (
        diagonal * (8 * diagonal * diagonal + 13 + diagonal * 15) * 2 + 3
    ) / 3

    return return_value


print(spiralize(501))

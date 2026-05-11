def verify_card_number(number: str()):
    new_number = number.replace(" ", "").replace("-", "")
    sum_of_elements = 0
    i = len(new_number) - 1
    odd = True
    while i >= 0:
        el = int(new_number[i])
        if odd:
            sum_of_elements += el
        else:
            el *= 2
            if el > 9:
                sum_of_elements += el - 9
            else:
                sum_of_elements += el
        odd = not odd
        i -= 1
    if sum_of_elements % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'


if __name__ == '__main__':
    assert verify_card_number('453914889') == 'VALID!'
    assert verify_card_number('4111-1111-1111-1111') == 'VALID!'
    assert verify_card_number('453914881') == 'INVALID!'
    assert verify_card_number('1234 5678 9012 3456') == 'INVALID!'

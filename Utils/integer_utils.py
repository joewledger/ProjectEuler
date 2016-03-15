def convert_int_to_digit_list(n):
    digits = []
    while(n > 0):
        digits.append(n % 10)
        n /= 10
    return list(reversed(digits))

def convert_digit_list_to_int(l):
    n = 0
    for index, element in enumerate(l):
        n += element * 10 ** (len(l) - index - 1)
    return n

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

def is_pandigital_integer_list(l,lower,upper):
    digit_set = set(digits)
    return all(lower <= n <= upper for n in digits) and len(digits) == (upper - lower + 1) and len(digits) == len(digit_set)

def is_pandigital(n,lower,upper):
    return is_pandigital_integer_list(convert_int_to_digit_list(n),lower,upper)

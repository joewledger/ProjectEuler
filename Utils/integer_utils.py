import math
class Big_Int:

    def __init__(self,digit_list):
        self.digit_list = digit_list

    def __len__(self):
        return len(self.digit_list)

def int_to_binary_digit_list(n):
    binary_length = int(math.log(n,2)) + 1
    digits = []
    for i in xrange(0,binary_length):
        place_value = 2 ** (binary_length - i - 1)
        if(n >= place_value):
            digits.append(1)
            n -= place_value
        else:
            digits.append(0)
    return digits
        

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

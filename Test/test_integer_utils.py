import Utils.integer_utils as utils

def test_int_to_binary_digit_list():
    assert [1,0,0,0,0] == utils.int_to_binary_digit_list(16)
    assert [1,1,1,0] == utils.int_to_binary_digit_list(14)

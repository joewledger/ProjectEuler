import Utils.combinatorics_utils as c

def test_get_linear_combinations():
    print(list(c.get_integer_linear_combinations(2,3,10)))
    assert [5,7,8,9,10] == sorted(list(c.get_integer_linear_combinations(2,3,11)))

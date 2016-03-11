import Utils.prime_utils as p


def test_get_num_divisors():
    util = p.Prime_Utils()
    for i in xrange(2,1001):
        nd = sum(1 for j in xrange(1, i + 1) if i % j == 0)
        nd2 = util.get_num_divisors(i)
        assert nd == nd2


def test_get_divisor_list():
    util = p.Prime_Utils()
    
    assert [1,2,4,5,10,20] == sorted(util.get_divisor_list(20))
    assert [1,2,3,6,9,18] == sorted(util.get_divisor_list(18))
    assert [1,3,5,15] == sorted(util.get_divisor_list(15))

def test_get_perfect_numbers():
    util = p.Prime_Utils()

    perfect_gen = util.get_perfect_numbers()
    assert 6 == perfect_gen.next()
    assert 28 == perfect_gen.next()
    assert 496 == perfect_gen.next()
    assert 8128 == perfect_gen.next()

import Utils.prime_utils as p


def test_get_num_divisors():
    util = p.Prime_Utils()
    for i in xrange(2,1001):
        nd = sum(1 for j in xrange(1, i + 1) if i % j == 0)
        nd2 = util.get_num_divisors(i)
        assert nd == nd2

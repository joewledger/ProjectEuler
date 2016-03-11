def get_integer_linear_combinations(a,b,threshold, min_a_coef=1,min_b_coef=1):
    a_coef = min_a_coef
    b_coef = min_b_coef
    combination = lambda va,vb,ca,cb : va * ca + vb * cb
    under_threshold = lambda va,vb,ca,cb,threshold : combination(va,vb,ca,cb) < threshold
    while(under_threshold(a,b,a_coef,b_coef,threshold)):
        while(under_threshold(a,b,a_coef,b_coef,threshold)):
            yield combination(a,b,a_coef,b_coef)
            b_coef += 1
        b_coef = min_b_coef
        a_coef += 1

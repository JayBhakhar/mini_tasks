def prime_factorization(n):
    i = 2
    factors = []
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
        # if n > 1:
        #     factors.append(n)
    return factors

a = prime_factorization(375)
print(a)


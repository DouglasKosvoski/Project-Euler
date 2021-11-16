
# Find largest prime factor
def prime_factors(n):
    aux, i = n, 2
    prime_factors = []
    while i < int(n**0.5)+1:
        if aux % i == 0:
            aux /= i
            prime_factors.append(i)
        else:
            i += 1
    # remove duplicates and return a list with all prime factors
    return list({i:i for i in prime_factors}.values())

primes = prime_factors(600851475143)
print(max(primes))

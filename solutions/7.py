def is_prime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    return prime

def solve(n):
    i = 1
    counter = 0
    while counter < n:
        i += 1
        if is_prime(i):
            counter += 1
    return i

n = 10001
print(solve(n))

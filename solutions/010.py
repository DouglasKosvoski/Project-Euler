
def is_prime(n):
    if n == 2 or n == 1:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solve(limit):
    sum = 0
    for i in range(2, limit):
        if (is_prime(i)):
            sum += i
    return sum

limit = 2000000
answer = solve(limit)
print(f"Total: {answer}")

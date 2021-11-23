
def check(n, upper):
    for i in range(upper, 0, -1):
        if n % i != 0:
            return False
    return True

def find(upper):
    found = False
    n = 0
    while not found:
        n += 2520
        found = check(n, upper)
    return n

upperlimit = 20
n = find(upperlimit)
print(n)

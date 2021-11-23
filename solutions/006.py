
def solve(limit=10):
    sum = 0
    squares = 0
    for i in range(1, limit+1):
        sum += i
        squares += (i**2)
    return abs(sum**2 - squares)

limit = 100
answer = solve(limit)
print(f"{answer}")

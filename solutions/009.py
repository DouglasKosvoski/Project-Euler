
def find_triplet(sum):
    for a in range(1, int(sum / 3)):
        for b in range(a + 1, int((sum - a) / 2)):
            c = sum - a - b
            if (a + b + c == sum ) and (a**2 + b**2 == c**2):
                return (a * b * c)
    return -1

answer = find_triplet(1000)
print(answer)

sum = 0
upperrange = 1000
for i in range(upperrange-1, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

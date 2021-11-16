
a = 1
b = 2
upperrange = 4000000
sum_of_evens = 0
while True:
    if a % 2 == 0: sum_of_evens += a
    if b % 2 == 0: sum_of_evens += b

    print(a, b, end=" ")
    if a + b < upperrange:
        a += b
        b += a
    else:
        break

print(f"\n\nSum of Evens: {sum_of_evens}")

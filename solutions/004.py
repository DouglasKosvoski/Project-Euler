
def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

def find_largest_palindrome(n_char=2):
    # yes, is "9"*2 = "99", "9"*3 = "999"...
    max_possible_number = int(str(9)*n_char)
    end = int(max_possible_number*0.9)-1
    palindrome = 0

    for i in range(max_possible_number, end, -2):
        for j in range(i, end, -2):
            if i*j > palindrome and is_palindrome(i*j):
                palindrome = i*j
                # print(f"{i} x {j} = {i*j}")

    return palindrome

# Find the largest palindrome made from the product of two 3-digit numbers
largest = find_largest_palindrome(4)
print(largest)

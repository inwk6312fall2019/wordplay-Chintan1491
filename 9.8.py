#prog 9.8
def is_palindrome(char):
    return char == char[::-1]

def odometer_number(number):
    if is_palindrome(str(number)[2:]):
        number += 1
        if is_palindrome(str(number)[1:]):
            number += 1
            if is_palindrome(str(number)[1:5]):
                number += 1
                if is_palindrome(str(number)):
                    return True
    return False

for n in range(100000,1000000):
    if odometer_number(n):
        print(n)

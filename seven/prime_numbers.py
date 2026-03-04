import math


def prime_checker(number):
    is_prime = True
    for x in range(2, math.floor(number / 2)):
        if number % x == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())
prime_checker(number=n)
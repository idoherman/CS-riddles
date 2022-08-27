import math


def is_prime_num(num):
    is_prime = True
    num_after_sqrt = int(math.sqrt(num)) + 1
    for i in range(2, num_after_sqrt, 1):
        if num % i == 0:
            # print(f"The numbers: {i}, {num // i} are factors of the num: {num}")
            is_prime = False
    return is_prime


def is_prime_factor(num):
    is_prime = True
    max_factor = 0
    num_after_sqrt = int(math.sqrt(num)) + 1
    for i in range(2, num_after_sqrt, 1):
        if num % i == 0:
            print(f"The numbers: {i}, {num // i} are factors of the num: {num}")
            is_prime = False

            if i > max_factor:
                if is_prime_num(i):
                    max_factor = i

            if (num // i) > max_factor:
                if is_prime_num(num // i):
                    max_factor = num // i

    print(f"\n \n The max factor of the num: {num} is: {max_factor}")
    return is_prime


if __name__ == '__main__':
    print(f"\n {is_prime_factor(600851475143)}")
    # print(is_prime_num(6857))


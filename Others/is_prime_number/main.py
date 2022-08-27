import math


def is_prime_num(num):
    is_prime = True
    num_after_sqrt = int(math.sqrt(num)) + 1
    for i in range(2, num_after_sqrt, 1):
        if num % i == 0:
            print(f"The numbers: {i}, {num // i} are factors of the num: {num}")
            is_prime = False
    return is_prime


if __name__ == '__main__':
    print(f"\n {is_prime_num(54260411971)}")

def multiples_of_3_and_5(max):
    sum = 0
    for i in range(1, 1000, 1):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    print(multiples_of_3_and_5(1000))

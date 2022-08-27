# return the sum of the even numbers in the
# Fibonacci sequence that are smaller than 4 milion
def sum_of_even_nums_fibonacci():
    sum = 0
    fibonacci_under_4_milion = [1, 2]
    num = 0
    index = 1
    while num < 4000000:
        num = fibonacci_under_4_milion[index - 1] + fibonacci_under_4_milion[index]
        fibonacci_under_4_milion.append(num)
        index += 1

    for i in fibonacci_under_4_milion:
        if i % 2 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    print(sum_of_even_nums_fibonacci())

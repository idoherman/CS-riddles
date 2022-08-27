def is_palindrome(num):
    num_string = str(num)
    return num_string == num_string[::-1]


def largest_palindrome_3_digits():
    largest_palindrome_found = -1
    digit_1 = 1
    digit_2 = 1



    # for i in range(999**2):
    #     digits_num = digit_1 * digit_2
    #
    #     if digits_num > largest_palindrome_found:
    #         if is_palindrome(digits_num):
    #             largest_palindrome_found = digits_num
    #
    #     if digit_1 < 999:
    #         digit_1 += 1
    #     else:
    #         digit_2 += 1
    #         digit_1 = 1

    return largest_palindrome_found


if __name__ == '__main__':
    print(largest_palindrome_3_digits())

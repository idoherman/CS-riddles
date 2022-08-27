def lengthOfLongestSubstring(s):
    current_length = 1
    max_length = 1
    str_for_check = s[0]
    for i in s[1::]:

        for j in range(len(str_for_check)):
            if str_for_check[j] == i:
                if current_length > max_length:
                    max_length = current_length

                current_length = 0
                str_for_check = ""
                break
        str_for_check += i
        current_length += 1
    if current_length > max_length:
        return current_length
    return max_length


if __name__ == '__main__':
    print(lengthOfLongestSubstring("dvdc"))

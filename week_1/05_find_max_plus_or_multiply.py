input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    # my code
    # max_result = array[0]
    # for num in array[1:]:
    #     # print(num)
    #     if num == 0 or num == 1:
    #         max_result += num
    #     elif max_result == 0 or max_result == 1:
    #         max_result += num
    #     else:
    #         max_result *= num
    #
    # return max_result

    # given code
    multiply_sum = 0
    for number in array: # array 길이 만큼 반복 -> O(N)
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)

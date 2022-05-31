input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!

    # my code
    # for i in array:
    #     if i != number:
    #         continue
    #     else:
    #         return True
    #
    # return False

    # given
    for element in array: # array의 길이만큼 아래 연산 실행
        if number == element: # 비교 연산 1번 실행
            return True       # N * 1 = N 만큼

        return False
    # Big-O: O(N)
    # Big-Omega: Om(1)

result = is_number_exist(3, input)
print(result)
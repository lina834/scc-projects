input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]
    for i in array:
        if i > max_num:
            max_num = i
    return max_num

    # for num in array:
    #     for compare_num in array:
    #         if num < compare_num:
    #             break
    #     else:
    #         # for 끝날때까지 break가 나오지 않았을때 실행됨
    #         return num


result = find_max_num(input)
print(result)
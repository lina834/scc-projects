input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    # 내 코드
    # for i in range(n):
    #     min_idx = i
    #     for j in range(i+1, n):
    #         if array[j] < array[min_idx]:
    #             min_idx = j
    #     array[i], array[min_idx] = array[min_idx], array[i]

    # 준 코드
    for i in range(n-1):  # 0 1 2 3
        min_idx = i
        for j in range(n-i):  #
            if array[i+j] < array[min_idx]:
                array[i+j], array[min_idx] = array[min_idx], array[i+j]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
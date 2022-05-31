input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    # 내 코드
    # n = len(array)
    # while n > 1:
    #     for i in range(1, n):
    #         if array[i - 1] > array[i]:
    #             array[i], array[i - 1] = array[i - 1], array[i]
    #     n -= 1

    # 준 코드
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

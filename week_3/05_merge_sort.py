array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    print(array)
    print('left_arary', left_array)
    print('right_arary', right_array)
    return merge(merge_sort(left_array), merge_sort(right_array))

# 출력된 값을 보면 다음과 같습니다!
# [5, 3, 2, 1, 6, 8, 7, 4]     맨 처음 array 이고,
# left_arary [5, 3, 2, 1]      이를 반으로 자른 left_array
# right_arary [6, 8, 7, 4]     반으로 자른 나머지가 right_array 입니다!

# [5, 3, 2, 1]                 그 다음 merge_sort 함수에는 left_array 가 array 가 되었습니다!
# left_arary [5, 3]            그리고 그 array를 반으로 자르고,
# right_arary [2, 1]           나머지를 또 right_array 에 넣은 뒤 반복합니다.

# [5, 3]
# left_arary [5]
# right_arary [3]

# [2, 1]
# left_arary [2]
# right_arary [1]

# [6, 8, 7, 4]
# left_arary [6, 8]
# right_arary [7, 4]

# [6, 8]
# left_arary [6]
# right_arary [8]

# [7, 4]
# left_arary [7]
# right_arary [4]
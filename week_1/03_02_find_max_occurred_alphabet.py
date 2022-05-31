import numpy as np

input = "hello my name is sparta"
alphabet_occurrence_array = [0] * 26


def find_max_occurred_alphabet(string):
    # 내 코드
    # for char in string:
    #     if not char.isalpha():
    #         continue
    #     idx = ord(char) - ord("a")
    #     alphabet_occurrence_array[idx] += 1
    # max_occurred_num = np.amax(alphabet_occurrence_array)
    # max_occurred_idx = alphabet_occurrence_array.index(max_occurred_num)
    # max_occurred = chr(max_occurred_idx + ord("a"))
    #
    # return max_occurred

    # given method 2
    for char in string:
        if not char.isalpha():  # 알파벳 일 때만 확인 후 배열 증가
            continue
        # 해당 알파벳의 acii 코드 이용해 배열 index 찾기
        idx = ord(char) - ord("a")
        alphabet_occurrence_array[idx] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)

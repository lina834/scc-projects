import numpy as np

input = "hello my name is sparta"
alphabet_occurrence_array = [0] * 26


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

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

    # given method 1
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet
    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)

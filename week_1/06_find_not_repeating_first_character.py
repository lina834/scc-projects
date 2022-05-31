input = "abadabac"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    # my code
    # alphabet_array = [0] * 26
    # for char in string:
    #     idx = ord(char) - ord("a")
    #     alphabet_array[idx] += 1
    #
    # # get list of all indices where char has occurred once
    # non_repeating_char_list = [i for i, x in enumerate(alphabet_array) if x == 1]
    # for char in string:
    #     for i in non_repeating_char_list:
    #         i_get_char = chr(i + ord("a"))
    #         if char == i_get_char:
    #             return char

    # given code
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():  # 알파벳 일 때만 확인 후 배열 증가
            continue
        # 해당 알파벳의 acii 코드 이용해 배열 index 찾기
        idx = ord(char) - ord("a")
        alphabet_occurrence_array[idx] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_character(input)
print(result)

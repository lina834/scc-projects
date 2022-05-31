def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha(): # 알파벳 일 때만 확인 후 배열 증가
            continue
        # 해당 알파벳의 acii 코드 이용해 배열 index 찾기
        idx = ord(char) - ord("a")
        alphabet_occurrence_array[idx] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
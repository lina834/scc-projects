input = "0001100"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    curr_num = "-"
    count_division_zero, count_division_one = 0, 0

    # check division pattern of string
    for idx, num in enumerate(string):
        if num == curr_num:
            continue
        else:  # if division detected
            if num == "0":
                count_division_zero += 1
            else:
                count_division_one += 1
            curr_num = num

    # flip number with less division
    # thus the least number of flip would be number of least division

    return min(count_division_zero, count_division_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
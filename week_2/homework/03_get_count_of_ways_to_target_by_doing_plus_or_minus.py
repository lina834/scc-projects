numbers = [1, 1, 1, 1, 1]
target_number = 3
result = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, curr_idx, curr_sum):
    # 구현해보세요!
    if curr_idx == len(array):
        if curr_sum == target:
            global result
            result += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, curr_idx+1, curr_sum+array[curr_idx])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, curr_idx+1, curr_sum-array[curr_idx])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(result)
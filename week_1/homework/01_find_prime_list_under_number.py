input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    for num in range(2, number):
        # check for 2 inside for loop in case number < 2
        if num == 2:
            prime_list.append(num)
        else:
            # check other cases
            is_prime = True
            for prime in prime_list:
                if num % prime == 0:  # divisible by existing prime -> meaning num is not prime number
                    is_prime = False
            if is_prime:
                prime_list.append(num)

    return prime_list


result = find_prime_list_under_number(input)
print(result)

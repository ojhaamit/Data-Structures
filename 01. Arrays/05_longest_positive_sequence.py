def positive_sequence(array):
    len_array = len(array)

    start_index = 0
    end_index = 0
    max_length = 0
    curr_length = 0

    result = []

    for i in range(len_array):
        if array[i] > 0:
            curr_length += 1
        else:
            if curr_length > max_length:
                max_length = curr_length
                end_index = i
                start_index = end_index - max_length
            curr_length = 0

    result.append([max_length, start_index])
    return result


if __name__ == "__main__":
    nums = [2, 3, -1, 4, 5, 2, -3, 1, 2, 3, 4, 5, -6, 2, 3]
    result = positive_sequence(nums)
    print(result)
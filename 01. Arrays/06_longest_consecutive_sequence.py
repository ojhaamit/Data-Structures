def longest_sequence(nums):
    len_array = len(nums)

    #sort the array first
    nums.sort()
    new_nums = []

    for i in range(len_array):
        if nums[i] not in new_nums:
            new_nums.append(nums[i])

    result = 0
    count_length = 0
    len_new_nums = len(new_nums)

    for i in range(len_new_nums):
        if i > 0 and new_nums[i] == new_nums[i-1] + 1:
            count_length += 1
        else:
            count_length = 1
        result = max(result, count_length)
   
    return result


if __name__ == "__main__":
    nums = [8, 8, 9, 9, 3, 4]
    result = longest_sequence(nums)
    print(result)
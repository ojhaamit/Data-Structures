def max_sum_subarray(nums):
    len_array = len(nums)

    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len_array):
        if current_sum > 0:
            current_sum += nums[i]
        else:
            current_sum = nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
        # current_sum = 0

    return max_sum

if __name__ == "__main__":
    nums = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    result = max_sum_subarray(nums)
    print(result)
def max_sub_array(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(len(nums)):
        if current_sum > 0:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_sub_array(nums)
    print(result)
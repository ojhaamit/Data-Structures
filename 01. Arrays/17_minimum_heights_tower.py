def minHeights(nums, k):
    len_nums = len(nums)
    nums.sort()
    curr_max = nums[len_nums - 1]
    curr_min = nums[0]
    result = curr_max - curr_min

    for i in range(1, len_nums):
        curr_max = max(nums[i-1] + k, nums[len_nums - 1] - k)
        curr_min = min(nums[i]-k, nums[0] + k)
        result = min(result, curr_max - curr_min)
    
    return result

if __name__ == '__main__':
    nums = [1, 5, 8, 10]
    k = 2
    result = minHeights(nums, k)
    print(result)
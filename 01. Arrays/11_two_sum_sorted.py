def two_sum_sorted(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        if nums[start] + nums[end] > target:
            end -= 1
        elif nums[start] + nums[end] < target:
            start += 1
        if nums[start] + nums[end] == target:
            return [nums[start], nums[end]] 

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18

    result = two_sum_sorted(nums, target)
    print(result)
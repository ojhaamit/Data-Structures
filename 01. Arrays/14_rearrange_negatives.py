def reArrangeNegatives(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] < 0:
            left += 1
        elif nums[right] > 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    
    return nums

if __name__ == "__main__":
    nums = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    result = reArrangeNegatives(nums)
    print(result)
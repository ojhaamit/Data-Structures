def twoSum(nums, target):
    num_set = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_set:
            return [nums[i], complement]
        num_set[nums[i]] = nums[i]

    return False

if __name__ == "__main__":
    nums = [2, 1, 5, 3]
    target = 4
    result = twoSum(nums, target)
    print(result)
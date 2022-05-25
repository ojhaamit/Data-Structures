def subArray(nums):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            result.append(nums[i:j])

    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subArray(nums)
    print(result)
def summaryRanges(nums):
    range_nums = []

    left = 0
    for right in range(len(nums)):
        if right + 1 == len(nums) or nums[right] +1 != nums[right + 1]:
            if left != right:
                range_nums.append(str(nums[left]) + '->' + str(nums[right]))
            else:
                range_nums.append(str(nums[left]))
            left = right + 1
    return range_nums 
        
if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]
    # print("main")
    result = summaryRanges(nums)
    print(result)
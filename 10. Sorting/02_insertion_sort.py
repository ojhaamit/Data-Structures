def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            swap(j, j-1, nums)
            j -= 1
    return nums

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
    nums = [8, 5, 9, 2, 5, 6, 3]
    result = insertionSort(nums)
    print(result)
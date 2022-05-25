def bubbleSort(nums):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                swap(i, i+1, nums)
                isSorted = False

    return nums

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
    nums = [8, 5, 9, 2, 5, 6, 3]
    result = bubbleSort(nums)
    print(result)
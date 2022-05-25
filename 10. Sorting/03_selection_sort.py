def selectionSort(nums):
    # swap_index = 0
    for i in range(len(nums)):
        swap_index = i
        for j in range(i+1, len(nums)):
            if nums[swap_index] > nums[j]:
                swap_index = j
        swap(i, swap_index, nums)

    return nums

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
    nums = [8, 5, 2, 9, 6, 5, 3]
    result = selectionSort(nums)
    print(result)
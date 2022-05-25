def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

def reverse(beg, end, nums):
    while beg < end:
        swap(beg, end, nums)
        beg += 1
        end -= 1

def nextPermutations(nums):
    len_array = len(nums)
    
    idx1 = -1
    for i in range(len_array - 1, 0, -1):
        if nums[i-1] < nums[i]:
            idx1 = i
            break

    if idx1 == -1:
        reverse(0, len_array-1, nums)
        return

    idx2 = len_array - 1
    while nums[idx1 - 1] >= nums[idx2]:
        idx2 -= 1

    swap(idx1-1, idx2, nums)
    reverse(idx1, len_array-1, nums)

    return nums

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = nextPermutations(nums)
    print(result)
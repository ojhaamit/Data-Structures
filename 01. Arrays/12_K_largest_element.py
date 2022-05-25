def kLargestElement(nums, k):
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l

        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        print(nums)
        nums[p], nums[r] = nums[r], nums[p]
        print(nums)
        if k < p:
            return quickSelect(l, p-1)
        elif k > p:
            return quickSelect(p+1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums)-1)


if __name__ == "__main__":
    nums = [5,2,4,1,3,6,0]
    k = 4
    result = kLargestElement(nums, k)
    print(result)
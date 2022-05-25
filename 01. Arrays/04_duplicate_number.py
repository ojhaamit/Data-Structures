def find_duplicate(nums):
    len_array = len(nums)
    visited_set = {}
    dup_number = 0

    for i in range(len_array):
        if nums[i] in visited_set:
            visited_set[nums[i]] = True
            dup_number = nums[i]
            break
        visited_set[nums[i]] = False
    
    return dup_number

if __name__ == "__main__":
    nums = [1,3,4,2,2]
    result = find_duplicate(nums)
    print(result)
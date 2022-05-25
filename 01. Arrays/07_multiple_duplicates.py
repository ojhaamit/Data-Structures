def duplicates(nums):
    len_array = len(nums)

    visited_set = {}
    result = []

    nums.sort()
    # print(nums)
    for i in range(len_array):
        if nums[i] in visited_set:
            visited_set[nums[i]] = True
            # result.append(nums[i])
        else:
            visited_set[nums[i]] = False
    
    for index, value in enumerate(visited_set):
        if visited_set[value] == True:
            result.append(value)

    print(result)
    
    return result

if __name__ == "__main__":
    nums = [10, 10, 7, 7, 7, 4, 0, 5, 10, 5, 10]
    result = duplicates(nums)
    print(result)
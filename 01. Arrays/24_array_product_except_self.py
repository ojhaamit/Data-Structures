def arrayProductExceptSelf(nums):
    len_array = len(nums)
    left = 1
    right = 1

    result = [1]

    for i in range(len_array - 1, 0, -1):
        right = right * nums[i]
        result.append(right)
    
    result = result[::-1]

    for i in range(len_array):
        result[i] = result[i] * left
        left = left * nums[i]
    return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = arrayProductExceptSelf(nums)
    print(result)
def maxProductArray(nums):
    max_product = max(nums)
    curr_max, curr_min = 1, 1

    for n in nums:
        if n == 0:
            curr_max, curr_min = 1, 1
            continue

        temp = curr_max * n
        curr_max = max(n*curr_max, n*curr_min, n)
        curr_min = min(temp, n*curr_min, n)
        max_product = max(max_product, curr_max)

    return max_product

if __name__ == "__main__":
    nums = [2,3,-2,4]
    result = maxProductArray(nums)
    print(result)
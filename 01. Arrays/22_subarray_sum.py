def subArraySum(nums, sum):
    curr_sum = 0
    start = 0
    end = -1

    sum_set = {}

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum - sum == 0:
            start = 0
            end = i
            break

        if (curr_sum - sum) in sum_set:
            start = sum_set.get(curr_sum - sum) + 1
            end = i
            break

        sum_set[curr_sum] = i

    if end == -1:
        return [-1, -1]
    else:
        return [start, end]

if __name__ == "__main__":
    nums = [4, 2, -3, 1, 6]
    sum = 0
    result = subArraySum(nums, sum)
    print(result)
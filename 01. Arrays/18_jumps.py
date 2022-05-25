def canJump(nums, n):
    goal = n - 1

    for i in range(n - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False
    
if __name__ == "__main__":
    nums = [3, 2, 1, 1, 4]
    n = len(nums)
    result = canJump(nums, n)
    print(result)
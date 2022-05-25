def house_robber(nums):
    rob1, rob2 = 0, 0

    for i in nums:
        temp = max(i + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return temp

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    result = house_robber(nums)
    print(result)
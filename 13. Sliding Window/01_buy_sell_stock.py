def buy_sell_stocks(nums):
    len_stocks = len(nums)

    if len_stocks == 0:
        return

    start = 0
    end = 1
    max_profit = 0
    curr_profit = 0

    while end < len_stocks:
        curr_profit = nums[end] - nums[start]

        if nums[start] > nums[end]:
            start = end

        if curr_profit > max_profit:
            max_profit = curr_profit
        curr_profit = 0
        end += 1

    return max_profit   


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    result = buy_sell_stocks(nums)
    print(result)
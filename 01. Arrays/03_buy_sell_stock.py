def maxProfit(prices):
    len_array = len(prices)
    print(prices)

    if len_array == 0:
        return 0

    start = 0
    end = 1
    max_profit = 0

    while end < len_array:
        if prices[end] - prices[start] > max_profit:
            max_profit = prices[end] - prices[start] 

        if prices[start] > prices[end]:
            start = end
        end += 1

    print(max_profit)
    return max_profit 

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    result = maxProfit(prices)
    print(result)


#Time Complexity: O(n)
#Space Complexity: O(1)
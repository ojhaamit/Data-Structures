class Solution:
    def searchRangeLinearTime(self, array, target):
        result = []
        for i in range(len(array)):
            if array[i] == target:
                result.append(i)

        return result if len(result) > 0 else [-1, -1]

    def searchRangeBinary(self, array, target):
        first = self.binarySearch(array, 0, len(array) - 1, target, True)
        last = self.binarySearch(array, 0, len(array) - 1, target,False)
        return [first, last]

    def binarySearch(self, array, low, high, target, findFirst):
        if high < low:
            return -1
        
        mid = low + (high - low) // 2

        if findFirst:
            if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
                return mid
            elif target > array[mid]:
                return self.binarySearch(array, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(array, 0, mid - 1, target, findFirst)

        else:
            if (mid == len(array) - 1 or target < array[mid + 1]) and array[mid] == target:
                return mid
            elif target < array[mid]:
                return self.binarySearch(array, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(array, mid + 1, high, target, findFirst)


array = [5,7,7,8,8,10]
target = 8

# result = Solution().searchRangeLinearTime(array, target)
result = Solution().searchRangeBinary(array, target)
print(result)
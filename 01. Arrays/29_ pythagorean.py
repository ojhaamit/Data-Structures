class Solution:
    def pythagorean(self, nums):
        square = set([num*num for num in nums])

        for a in nums:
            for b in nums:
                if a*a + b*b in square:
                    return True

        return False

nums = [3, 5, 12, 5, 13]
print(Solution().pythagorean(nums))
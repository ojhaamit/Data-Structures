class Solution:
    def permute(self, nums):
        return self.permuteHelper(nums)

    def permuteHelper(self, nums, start = 0):
        if start == len(nums):
            return [nums[:]]
        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self.permuteHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return result

    def permute2(self, nums, values = []):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i+1:], values + [nums[i]])
        return result

nums = [1,2, 3]
print(Solution().permute(nums))
print(Solution().permute2(nums))
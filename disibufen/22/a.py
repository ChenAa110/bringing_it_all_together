class Solution(object):
    def runningSum(self, nums):
        if not nums:
            return []

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums


nums=[1,2,3,4,5,]
s=Solution()
s.runningSum()
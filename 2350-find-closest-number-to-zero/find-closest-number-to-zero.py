class Solution(object):
    def findClosestNumber(self, nums):
        if not nums:
            return 0

        
        abs_nums = [abs(x) for x in nums]
        min_abs = min(abs_nums)

        if min_abs in nums:
            return min_abs
        return -min_abs



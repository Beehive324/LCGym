class Solution(object):
    def twoSum(self, nums, target):
        c_map = {}


        for i in range(len(nums)):
            c_map[nums[i]] = i
        

        for n in range(len(nums)):
            compliment = target - nums[n]

            if compliment in c_map and c_map[compliment] != n:
                return [n, c_map[compliment]]
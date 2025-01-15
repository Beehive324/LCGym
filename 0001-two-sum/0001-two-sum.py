class Solution(object):
    def twoSum(self, nums, target):
        compliment_map = {}

        for i in range(len(nums)):
            compliment_map[nums[i]] = i
        

        for n in range(len(nums)):
            compliment = target - nums[n]
            if compliment in compliment_map and n != compliment_map[compliment]:
                return [n, compliment_map[compliment]]
        
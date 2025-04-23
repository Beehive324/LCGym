class Solution(object):
    def twoSum(self, nums, target):

        comp_map = {}

        for i in range(len(nums)):
            comp_map[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in comp_map:
                if comp_map.get(comp) != i:
                    return [comp_map.get(comp), i]


        
class Solution(object):
    def twoSum(self, nums, target):
        """
        build up hashmap with index as the key and number as the arget

        go though nums if res = target - nums[i] is in the hashmap

        return i and hashamp.get(res)
        """
        compliment_map = {}

        for i in range(len(nums)):
            compliment_map[nums[i]] = i
        
        for i in range(len(nums)-1):
            res = target - nums[i]
            if res in compliment_map.keys() and i != compliment_map.get(res): #no 2 indexes are the same
                return [i, compliment_map.get(res)]
        
        


        
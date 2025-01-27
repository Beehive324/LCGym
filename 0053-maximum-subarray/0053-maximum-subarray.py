class Solution(object):
    def maxSubArray(self, nums):
        #Sliding Window Problem
        #BFS
        #DFS
        #Binary Search
        max_sum = float('-inf')

        l = 0

        while l < len(nums):
            for i in range(len(nums)):
                new_sum = nums[l:i+1]
                if new_sum:
                    max_sum = max(sum(new_sum), max_sum)

            l += 1
        
        return max_sum
        
        
       
        
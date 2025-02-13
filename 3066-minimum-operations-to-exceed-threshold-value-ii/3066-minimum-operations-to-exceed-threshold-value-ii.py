class Solution(object):
    def minOperations(self, nums, k):

        heapq.heapify(nums)
   
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            count += 1
        

        return count

        
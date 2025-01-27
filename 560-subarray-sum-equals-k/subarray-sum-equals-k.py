class Solution(object):
    def subarraySum(self, nums, k):
        current_sum = 0
        res = 0
        freq_map = {}


        for num in nums:
            current_sum += num

            if current_sum == k:
                res += 1
            

            diff = current_sum - k

            if diff in freq_map:
                res += freq_map[diff]
            

            freq_map[current_sum] = freq_map.get(current_sum, 0) + 1
        

        return res

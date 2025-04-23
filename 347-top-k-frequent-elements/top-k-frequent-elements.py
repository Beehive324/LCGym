class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = {}
        res = []

        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        
        freq_map = sorted(freq_map.items(), key = lambda x: x[1], reverse=True)

        for value, freq in freq_map:
            res.append(value)

        return res[:k]




        
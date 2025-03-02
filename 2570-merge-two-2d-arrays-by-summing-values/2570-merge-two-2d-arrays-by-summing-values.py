class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        maps = {}

        for i in range(len(nums1)):
            maps[nums1[i][0]] = nums1[i][1]
        
        for j in range(len(nums2)):
            if nums2[j][0] in maps:
                a = maps.get(nums2[j][0])
                maps[nums2[j][0]] = nums2[j][1] + maps.get(nums2[j][0], 0)
            else:
                maps[nums2[j][0]] = nums2[j][1]
        
        for key, value in maps.items():
            res.append([key, value])
        

        res.sort()

        return res



        
        
class Solution(object):
    def moveZeroes(self, nums):
        res = []
        zero_arr = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_arr.append(nums[i])
            else:
                res.append(nums[i])

        
        result = res + zero_arr

        nums[:] = result
            

        
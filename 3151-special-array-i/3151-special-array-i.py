class Solution(object):
    def isArraySpecial(self, nums):

        if not nums:
            return False

        def both_even(a, b):
            return (a % 2 == 0) and (b % 2 == 0)

        
        def both_odd(a, b):
            return (a % 2 != 0) and (b % 2 != 0)
             
        
        for i in range(1,len(nums)):
            if both_even(nums[i], nums[i-1]) or both_odd(nums[i], nums[i-1]):
                return False
        

        return True


        
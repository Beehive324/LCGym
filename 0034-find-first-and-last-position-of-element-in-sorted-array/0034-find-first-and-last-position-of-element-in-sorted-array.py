class Solution(object):
    def searchRange(self, nums, target):
        def first_pos(nums, target):
            l = 0
            r = len(nums) -1
            first = -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    first = m
                    r = m - 1 #start at the left half of the array
                
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return first
        
        def last_pos(nums, target):
            l = 0
            r = len(nums) -1
            last = -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    last = m
                    l = m + 1 #start at the second half
                
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return last
    

        first_el = first_pos(nums, target)
        last_el = last_pos(nums, target)


        return [first_el, last_el]
        
        
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        There are n kids with candles
        array of candies
        candies[i] number of candies of ith kid
        extraCandies, extra candies you have
        after giving ith kid, return true if the kid will have the greatest number of candies of all other kids, false 
        otherwise
        """
        true = True
        false = False
        res = []

        def is_greater(num, arr):
            for i in range(len(arr)):
                if num < arr[i]:
                    return False
            return True

        for candie in candies:
            added_candies = candie + extraCandies
            if is_greater(added_candies, candies):
                res.append(true)
            else:
                if not is_greater(added_candies, candies):
                    res.append(false)
            
        
        return res


        
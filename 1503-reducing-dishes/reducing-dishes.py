class Solution(object):
    def maxSatisfaction(self, satisfaction):

        satisfaction.sort(reverse=True)

        presum = 0
        res = 0

        for i in range(len(satisfaction)):
            presum += satisfaction[i]
            if presum < 0:
                continue
            res += presum #add to the result, the best possible value
        

        return res


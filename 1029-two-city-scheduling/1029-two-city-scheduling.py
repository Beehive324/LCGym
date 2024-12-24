class Solution(object):
    def twoCitySchedCost(self, costs):
        diff = []
        res = 0

        for cost_a, cost_b in costs:
            dif = (cost_b - cost_a)
            diff.append([dif, cost_a, cost_b])
        
        diff.sort()

        # if the cost_b - a is less than 0 then go b
        # if cost cost_b -a is > 0 then go a
        
        for i in range(len(diff)):
            # if i is less than halfway point of lis
            if i < len(diff) // 2:
                val = diff[i][2]
                res += val
            else:
                res += diff[i][1]
        

        return res



        


        




        
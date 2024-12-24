class Solution(object):
    def twoCitySchedCost(self, costs):
        diffs = []
        
        for c1, c2 in costs: #iterate through costs
            diffs.append([c2 - c1, c1, c2]) #calculate differences
        diffs.sort() #sore the array
        res = 0 #assign res to 0
        for i in range(len(diffs)): #iterate over diffs
            if i < len(diffs) // 2:
                res += diffs[i][2] #send to city 2
            else:
                res += diffs[i][1] #send to city 1
        return res #return res
        
        
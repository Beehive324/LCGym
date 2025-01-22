class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            last_el = res[-1][1]

            if intervals[i][0] <= last_el:
                res[-1][1] = max(intervals[i][1], last_el)
            else:
                res.append(intervals[i])
        

        return res


class Solution(object):
    def maxScoreSightseeingPair(self, values):

        max_score = 0

        i = 0
        j = 1

        while j <= len(values)-1:
            score = values[i] + values[j] + i - j
            max_score = max(score, max_score)


            if values[i] + i < values[j] + j:
                i = j
            j += 1
      

        return max_score

        
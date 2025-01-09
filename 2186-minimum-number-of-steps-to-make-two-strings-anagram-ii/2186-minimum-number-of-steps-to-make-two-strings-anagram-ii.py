class Solution(object):
    def minSteps(self, s, t):
        count = 0
        freq_s = {}
        freq_t = {}


        for i in range(len(s)):
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
        
        for j in range(len(t)):
            freq_t[t[j]] = 1 + freq_t.get(t[j], 0)

        
        for key in freq_s.keys():
            count += abs(freq_s.get(key, 0) - freq_t.get(key, 0))
        
        for key in freq_t.keys():

            if key not in freq_s.keys():

                count += freq_t.get(key, 0)
        

        return count
        
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        char_set = set()
        res = 0



        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            else:
                char_set.add(s[r])
            
            res = max(res, abs(r- l + 1))

        return res

class Solution(object):
    def firstUniqChar(self, s):

        char_map = {}

        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i], 0) + 1


        for i in range(len(s)):
            if char_map.get(s[i]) == 1:
                return i
        return -1


        

        
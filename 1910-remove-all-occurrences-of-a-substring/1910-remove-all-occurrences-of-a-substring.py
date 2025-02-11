class Solution(object):
    def removeOccurrences(self, s, part):


        while part in s:

            start_index = s.find(part)


            s = s[:start_index] + s[start_index + len(part):]
        

        return s
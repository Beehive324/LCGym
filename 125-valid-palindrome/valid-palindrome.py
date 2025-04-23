class Solution(object):
    def isPalindrome(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        print(s)
        start = 0
        end = len(s)-1

        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True

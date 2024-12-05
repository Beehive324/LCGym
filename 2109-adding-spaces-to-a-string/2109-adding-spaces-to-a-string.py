class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        sp_set = set(spaces)
        res = []
        for i in range(len(s)):
            if i in sp_set:
                res.append(" ")
                res.append(s[i])
            else:
                res.append(s[i])
        


        return "".join(res)

        
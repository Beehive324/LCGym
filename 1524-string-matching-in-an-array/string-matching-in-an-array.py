class Solution(object):
    def stringMatching(self, words):

        res = []

        for i in range(len(words)):
            for j in range(len(words)):

                if words[i] == words[j]:
                    continue
                
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        

        return res

        
class Solution(object):
    def detectCapitalUse(self, word):
        #first word has to be capital
        #all words are capial
        count = 0

        if len(word) == 1:
            return True

        if word.upper() == word:
            return True

        if word.lower() == word:
            return True
 
        def is_capital(s):
            if s.upper() == s:
                return True
            return False

        for i in range(len(word)):
            if is_capital(word[i]):
                count += 1
        

        return is_capital(word[0]) and count <= 1

    
        
        
        

        
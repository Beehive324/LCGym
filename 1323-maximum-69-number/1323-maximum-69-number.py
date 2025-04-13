class Solution(object):
    def maximum69Number (self, num):
        new_num = list(str(num))

        numbers = []


        for i in range(len(new_num)):
            if new_num[i] == "6":
                new_num[i] = "9"
                break
            
    
        return int(''.join(new_num))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       a=s.split()
       b=len(a[-1])
       return b

       """
       i = len(s) - 1
        length = 0
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
        """ 


        

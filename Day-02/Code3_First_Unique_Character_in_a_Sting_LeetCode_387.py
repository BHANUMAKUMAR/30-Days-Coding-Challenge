class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Brute Force
        for i in range(len(s)):
            is_unique=True
            for j in range(len(s)):
                if i!=j and s[i]==s[j]:
                    is_unique=False
                    break
            if is_unique:
                return i
        return -1"""
        #Optimal
        cc={}
        for char in s:
            cc[char]=cc.get(char,0)+1
        for i,char in enumerate(s):
            if cc[char]==1:
                return i
        return -1

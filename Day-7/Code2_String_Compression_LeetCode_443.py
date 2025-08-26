class Solution:
    def compress(self, chars: List[str]) -> int:
        """Brute Force
        s=""
        i=0
        n=len(chars)
        while i< n:
            count=1
            while i+1<n and chars[i]==chars[i+1]:
                count+=1
                i+=1
            s+=chars[i]
            if count>1:
                s+=str(count)
            i+=1
        c_len=len(s)
        for j in range(c_len):
            chars[j]=s[j]
        return c_len"""
        #optimal
        write=0
        i=0
        n=len(chars)
        while i< n:
            char=chars[i]
            count=1
            while i+1<n and chars[i]==chars[i+1]:
                count+=1
                i+=1
            chars[write]=char
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
            
            i+=1

        return write

        

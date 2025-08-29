class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            a=str(n)
            b=[]
            for i in a:
                c=int(i)
                b.append(c)
            c=0
            for i in b:
                c=c+(i)**2
            n=c

        return n==1


            
        

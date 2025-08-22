class Solution:
    def romanToInt(self, s: str) -> int:
        char_map={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total=0
        prev=0
        for i in reversed(s):
            vl=char_map[i]
            if vl<prev:
                total-=vl
            else:
                total+=vl
                prev=vl
        return total
        

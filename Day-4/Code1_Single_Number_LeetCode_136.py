class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """a=set(nums)
        for i in a:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count==1:
                b=i
                return b"""
        result=0
        for i in nums:
            result^=i
        return result

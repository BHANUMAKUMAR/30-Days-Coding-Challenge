class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        n2=2*n
        ans=[None] *(n2)
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans

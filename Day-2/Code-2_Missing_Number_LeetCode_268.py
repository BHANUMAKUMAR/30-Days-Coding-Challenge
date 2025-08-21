class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ##Brute Force
        ##for i in range(len(nums)+1):
            ##if i not in nums:
                ##return i
        ##Optimal
        a=len(nums)
        expected=(a*(a+1))//2
        actual=sum(nums)
        return expected-actual
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        for i in range(a):
            for j in range(i+1,a):
                if nums[i]==nums[j]:
                    return True
            else:
                return False
        
